import os

from keras.models import model_from_json
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
    print(os.getcwd())
    model = load_model_format()
    model.load_weights('../models/trained/weights/plant_maturity.h5')
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def load_model_format():
    json_file = open('../models/trained/format/plant_maturity.json', 'r')
    loaded_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_json)

    return loaded_model
