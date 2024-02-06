'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-02-06 13:09:10
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2024-02-06 16:21:47
FilePath: /smart_hydroponic_farm/src/Cloud_compute/ai_model_host/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI
# cors
from fastapi.middleware.cors import CORSMiddleware
from private_func import download_model
import uvicorn
import os
import requests
import torch
os.environ['KERAS_BACKEND'] = 'torch'
import keras
import numpy as np

print("torch version:", torch.__version__)
print("keras version:", keras.__version__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(data:dict):
    """
    data: dict
    {
        "username": "username",
        "repo_name": "repo_name",
        "model_name": "model_name",
        "input_data": "input_data"
    }
    """
    username = data['username']
    repo_name = data['repo_name']
    model_name = data['model_name']
    input_data = list(map(float, data['input_data'][1:-1].split(',')))
    model_path = download_model(username, repo_name, model_name)
    print(f"model at {model_path}")
    input_data = np.array(input_data).reshape(1, -1)
    if model_path.endswith('.keras'):
        loaded_model = keras.saving.load_model(model_path)
        result = loaded_model.predict(input_data)
        result = result.tolist()
    elif model_path.endswith('.pt'):
        model = torch.load(model_path)
        result = model(input_data)
        result = result.tolist()
    else:
        result = "Model type not supported"

    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)