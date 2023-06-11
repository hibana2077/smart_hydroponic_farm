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

    def preprocess(self, img_data):#it should be work
        '''
        Preprocess image
        '''
        # Read image
        img = cv.imdecode(np.frombuffer(img_data.read(), np.uint8), cv.IMREAD_COLOR)
        # Resize image
        img = cv.resize(img, (224, 224))
        # Reshape image
        img = img.reshape(1, 224, 224, 3)
        # Normalize image
        img = img / 255.0
        return img

    def predict(self, img_data):
        '''
        Predict image
        '''
        # Preprocess image
        img = self.preprocess(img_data)
        # Predict
        prediction = self.model.predict(img)
        # Get label
        label = self.labels[str(np.argmax(prediction))]
        return label