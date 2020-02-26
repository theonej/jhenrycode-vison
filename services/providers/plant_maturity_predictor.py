from keras import backend as backend

from .modelSingleton import modelSingleton
import numpy as np


def predict(image_matrix):
    
    model = modelSingleton.instance()
    
    batch = create_image_batch(image_matrix)

    prediction = model.predict(batch)
    
    return prediction

def create_image_batch(image_matrix):

    batch = np.full((1, image_matrix.shape[0], image_matrix.shape[1], image_matrix.shape[2]), 0)
    batch[0] = image_matrix

    return batch
