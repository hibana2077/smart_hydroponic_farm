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

