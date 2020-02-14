import os

from keras.models import load_model
import numpy as np

model = None

def predict(image_matrix):
    global model
    if model is None:
        model = load_trained_model()

    batch = create_image_batch(image_matrix)

    prediction = model.predict(batch)

    return prediction

def create_image_batch(image_matrix):

    batch = np.full((1, image_matrix.shape[0], image_matrix.shape[1], image_matrix.shape[2]), 0)
    batch[0] = image_matrix

    return batch

def load_trained_model():
    model = load_model('../models/trained/weights/plant_maturity.h5')

    return model
