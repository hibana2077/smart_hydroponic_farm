'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-02-06 14:18:08
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2024-02-06 16:23:38
FilePath: /smart_hydroponic_farm/src/Cloud_compute/ai_model_host/private_func.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import json

BASE_HF_MODEL_TABLE_URL = "https://huggingface.co/{username}/{repo_name}/raw/main/table.json"
BASE_HF_MODEL_DOWNLOAD_URL = "https://huggingface.co/{username}/{repo_name}/resolve/main/models/{model_file_name}?download=true"

def download_model(username:str, repo_name:str, model_name:str)->str:
    """
    Download a model from Hugging Face based on the provided username, repository name, and model name.

    Parameters:
    - username (str): The username of the model owner.
    - repo_name (str): The name of the repository where the model is located.
    - model_name (str): The name of the model to be downloaded.

    Returns:
    - str: The path to the downloaded model.

    Raises:
    - ValueError: If the model version is not found or there is an error with the model version.

    """
    # get index info from huggingface
    response = requests.get(BASE_HF_MODEL_TABLE_URL.format(username=username, repo_name=repo_name))
    index = response.json()
    last_version = float(index[model_name]['version'])
    local_record = f"models/table.json"
    #read local record
    with open(local_record, 'r') as f:
        local_index = f.read()
    local_index = json.loads(local_index)
    if model_name in local_index:
        if float(local_index[model_name]['version']) == last_version:
            print("Model already up to date")
            return local_index[model_name]['path']
        elif float(local_index[model_name]['version']) < last_version:
            print("Updating model")
            model_file_name = index[model_name]['path']
            url = BASE_HF_MODEL_DOWNLOAD_URL.format(username=username, repo_name=repo_name, model_file_name=model_file_name)
            response = requests.get(url)
            model_path = f"models/{model_file_name}"
            with open(model_path, 'wb') as f:
                f.write(response.content)
            local_index[model_name] = {
                "version": last_version,
                "path": model_path
            }
            with open(local_record, 'w') as f:
                f.write(json.dumps(local_index))
            return model_path
        else:
            print("Model version error")
            raise ValueError("Model version error")
    else:
        print("Downloading model")
        model_file_name = index[model_name]['path']
        url = BASE_HF_MODEL_DOWNLOAD_URL.format(username=username, repo_name=repo_name, model_file_name=model_file_name)
        response = requests.get(url)
        model_path = f"models/{model_file_name}"
        with open(model_path, 'wb') as f:
            f.write(response.content)
        local_index[model_name] = {
            "version": last_version,
            "path": model_path
        }
        with open(local_record, 'w') as f:
            f.write(json.dumps(local_index))
        return model_path