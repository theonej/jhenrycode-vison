import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import generators.model_data_generator as generator
import models.definitions.resnet.resnet50 as resnet

BATCH_SIZE = 16
TARGET_HEIGHT = 64
TARGET_WIDTH = 64

EPOCH_STEPS=500
EPOCHS=1
VALIDATION_STEPS=10

def train_model():

    model = resnet.create_model((TARGET_HEIGHT, TARGET_WIDTH, 3), classes=2)

    model.summary()

    train_gen, val_gen = generator.create_generators(BATCH_SIZE, './data/train/plant_maturity', './data/validation/plant_maturity', [TARGET_HEIGHT, TARGET_WIDTH])

    model.fit_generator(
            train_gen,
            steps_per_epoch=EPOCH_STEPS,
            epochs=EPOCHS,
            validation_data=val_gen,
            validation_steps=VALIDATION_STEPS
    )

    model_format = model.to_json()
    with open('./models/trained/format/resnet.json', 'w') as format_file:
        format_file.write(model_format)

    model.save_weights('./models/trained/weights/resnet.h5')

train_model()