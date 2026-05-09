from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No selected file"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Dummy AI Prediction
    prediction = "Tomato Leaf Blight"

    fertilizer = "Use organic compost + potassium fertilizer"

    return render_template(
        'index.html',
        prediction=prediction,
        fertilizer=fertilizer,
        image=filepath
    )

if __name__ == '__main__':
    app.run(debug=True)