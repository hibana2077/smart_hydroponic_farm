'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-03-10 13:49:11
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-06-11 10:54:43
FilePath: \基於滴灌式水耕農法之改進研究以及實作\Cloud_compute\api.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import uvicorn
import cv2 as cv
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request, Response, status, UploadFile, File

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

class Picture(BaseModel):
    picture: str

@app.post("/api/v1/object_detection")
async def object_detection(picture: Picture):
    return {"message": "Hello World"}
    #This function will use ml model to detect objects in the picture and return the result

@app.post("/api/v1/plant_classification")
async def plant_classification(file: UploadFile = File(...)):
    import plant_classfier as pc
    PC = pc.PlantClassifier()
    prediction = PC.predict(file.file)
    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)