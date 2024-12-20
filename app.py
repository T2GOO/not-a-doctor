from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import webbrowser

IMAGE_DIM = 200
MODEL_PATH = "model.h5"
CLASS_NAME = ('Covid', 'Normal', 'Viral Pneumonia')

app = Flask(__name__)

model = load_model(MODEL_PATH)

def prepare_image(image, target_size=(IMAGE_DIM, IMAGE_DIM)):
    image = image.resize(target_size)
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    return img_array

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "File not found"})
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty file name"})

    image = Image.open(file.stream).convert("RGB")
    img_array = prepare_image(image)
    predictions = model.predict(img_array).flatten()
    result = {f"{clas}": f"{round(float(pred)*100, 2)}%" for clas, pred in zip(CLASS_NAME, predictions)}
    return jsonify(result)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)
