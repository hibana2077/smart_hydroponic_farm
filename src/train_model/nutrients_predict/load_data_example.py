'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2024-02-09 22:57:01
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2024-02-09 23:03:19
FilePath: /smart_hydroponic_farm/src/train_model/nutrients_predict/load_data_example.py
Description: This is a example of how to load data from npz file you need to download npz file from https://huggingface.co/hibana2077/oasis/blob/main/data/nutrients_predict_data.npz
'''
import numpy as np

# load npz file
file_path = ""

# load data
data = np.load(file_path)

X_train = data['X_train']
y_train = data['y_train']
X_test = data['X_test']
y_test = data['y_test']