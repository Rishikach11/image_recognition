from flask import Flask, render_template, request, session
from flask_session import Session
import tensorflow as tf
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

model = load_model('cnn_cifar10_model.h5')
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


# Route to handle the homepage
@app.route('/')
def index():
    return render_template('index.html')

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

        # Predict the class
        predictions = model.predict(image)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = round(100 * np.max(predictions), 2)  # Calculate confidence

        # Store prediction history in session
        if 'history' not in session:
            session['history'] = []
        
        session['history'].append({
            'prediction': predicted_class,
            'confidence': confidence,
            'img_src': filepath
        })

        return render_template('index.html', prediction=predicted_class, confidence=confidence, img_src=filepath, history=session['history'])


if __name__ == '__main__':
    app.run(debug=True)
