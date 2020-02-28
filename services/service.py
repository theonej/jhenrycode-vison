import os
from flask import Flask, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
import uuid
import providers.plant_maturity_predictor as predictor

app = Flask(__name__)

@app.route('/prediction/plant_maturity', methods=['POST'])
def get_prediction():
    image_matrix = get_image_data(request)

    prediction = predictor.predict(image_matrix)

    return jsonify(prediction.tolist())

@app.route('/prediction/health-check', methods=['GET'])
def get_prediction():
    return jsonify("ok")

def get_image_data(request):
    image_file_data = request.files["image-data"]
    file_name = '{}.png'.format(uuid.uuid1())
    image_file_data.save(file_name)

    image = load_img(file_name, target_size=(256, 256))

    image_matrix = img_to_array(image)

    os.remove(file_name)

    return image_matrix
    

app.run(host="0.0.0.0", port=9001, threaded=False)
