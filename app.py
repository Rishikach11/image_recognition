from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load the trained model
model = load_model('cnn_cifar10_model.h5')

# Define the class names (same as in the model)
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
history = []  # To store prediction history

# Route to handle the homepage
@app.route('/')
def index():
    return render_template('index.html', history=history)

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('static', filename)
        file.save(filepath)

        # Preprocess the image
        image = Image.open(filepath).resize((32, 32))
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Predict the class and calculate confidence
        predictions = model.predict(image)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = round(np.max(predictions) * 100, 2)

        # Save prediction in history
        history.append({
            'image_name': filename,
            'prediction': predicted_class,
            'confidence': confidence
        })

        return render_template('index.html', prediction=predicted_class, confidence=confidence, img_src=filepath, history=history)

if __name__ == '__main__':
    app.run(debug=True)
