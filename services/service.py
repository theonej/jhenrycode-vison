import os
from flask import Flask, escape, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
import uuid
import providers.plant_maturity_predictor as plant_maturity_predictor

app = Flask(__name__)

@app.route('/plant_maturity/predict', methods=['POST'])
def get_prediction():
    image_matrix = create_image_batch(request)

    prediction = plant_maturity_predictor.predict(image_matrix)
    print(prediction)

    return jsonify(prediction.tolist())

def create_image_batch(request):
    image_matrix = get_image_data(request)

    return image_matrix

def get_image_data(request):
    image_file_data = request.files["image-data"]
    file_name = '{}.png'.format(uuid.uuid1())
    image_file_data.save(file_name)

    image = load_img(file_name, target_size=(256,256))
    print(image.size)
    
    image_matrix = img_to_array(image)
    print(image_matrix)

    #clean up
    os.remove(file_name)
    #return image matrix as an array so it increases dimensionality to 4
    return image_matrix