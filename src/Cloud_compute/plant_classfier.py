from tensorflow import keras
import tensorflow as tf
import numpy as np
import cv2 as cv
import os
import json

'''
Workflows(OOP):
    1. Load model
    2. Load image
    3. Preprocess image
    4. Predict
'''

#change to current file path
os.chdir(os.path.dirname(__file__))

#-----------------Constants-----------------
# Path to model
MODEL_PATH = '../model/plant_classifier.h5'
# Path to labels
LABEL_PATH = '../model/labels.json'
#-----------------Constants-----------------

#-----------------Class-----------------
class PlantClassifier:
    '''
    PlantClassifier class
    '''
    def __init__(self, model_path=MODEL_PATH, label_path=LABEL_PATH):
        '''
        Constructor
        '''
        self.model = keras.models.load_model(model_path)
        self.labels = json.load(open(label_path))

    def predict(self, img_path):
        '''
        Predict image
        '''
        img = cv.imread(img_path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.resize(img, (224, 224))
        img = np.reshape(img, (1, 224, 224, 3))
        img = img / 255.0
        prediction = self.model.predict(img)
        prediction = np.argmax(prediction)
        return self.labels[str(prediction)]