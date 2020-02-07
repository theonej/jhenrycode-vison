import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import generators.model_data_generator as generator

BATCH_SIZE = 16
TARGET_HEIGHT = 64
TARGET_WIDTH = 64

EPOCH_STEPS=500
EPOCHS=1
VALIDATION_STEPS=10

def train_model():

    train_gen, val_gen = generator.create_generators(BATCH_SIZE, './data/train/plant_maturity', './data/validation/plant_maturity', [TARGET_HEIGHT, TARGET_WIDTH])


train_model()