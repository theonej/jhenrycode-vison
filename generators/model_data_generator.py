import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

def create_generators(batch_size, train_path, validation_path, target_size):
    train_datagen = create_train_gen()
    val_datagen = create_val_gen()

    train_gen = train_datagen.flow_from_directory(train_path, target_size=target_size, batch_size=batch_size, class_mode='categorical')
    val_gen = val_datagen.flow_from_directory(train_path, target_size=target_size, batch_size=batch_size, class_mode='categorical')

    return [train_gen, val_gen]

def create_train_gen():
    train_gen = ImageDataGenerator(
        rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True
    )

    return train_gen

def create_val_gen():
    return ImageDataGenerator(rescale=1./255)
