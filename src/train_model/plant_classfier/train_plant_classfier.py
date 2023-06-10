import tensorflow as tf
import numpy as np
import cv2 as cv
import os
import sys

#change path to the directory of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#------------------Constants------------------
DATA_DIR_PATH = "../../data/PlantVillage"
X_TRAIN_PATH = DATA_DIR_PATH + "/X_train.npy"
Y_TRAIN_PATH = DATA_DIR_PATH + "/Y_train.npy"
X_TEST_PATH = DATA_DIR_PATH + "/X_test.npy"
Y_TEST_PATH = DATA_DIR_PATH + "/Y_test.npy"
MODEL_PATH = "../../models/plant_classifier.h5"
#---------------------------------------------

x_train = np.load(X_TRAIN_PATH)
y_train = np.load(Y_TRAIN_PATH)
x_test = np.load(X_TEST_PATH)
y_test = np.load(Y_TEST_PATH)

#------------------Show data------------------
print("x_train shape: ", x_train.shape)
print("y_train shape: ", y_train.shape)
print("x_test shape: ", x_test.shape)
print("y_test shape: ", y_test.shape)
#---------------------------------------------