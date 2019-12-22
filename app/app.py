import os
import tensorflow as tf
import numpy as np

from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename

from app.common import _preprocess_img, _map_pred_to_class

UPLOAD_FOLDER = 'C:\\Users\\md705\\OneDrive\\Documents\\FlaskDownloads\\'
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_SIZE'] = 16*1024*1024

model = None # Needed so defining the global variable doesn't raise an issue
def load_model():
    global model
    model_path = 'rowing_1213.h5'
    model = tf.keras.models.load_model(model_path)

def prediction(image):
    img_tensor = _preprocess_img(image)
    model_pred = model.predict(img_tensor)
    pred_class, prob = _map_pred_to_class(model_pred)
    return pred_class, round(prob, 3)

def allowed_file(filename):
    return ('.' in filename) and (filename!='') and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route('/', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            if allowed_file(image.filename):
                filename = secure_filename(image.filename)
                img_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
                image.save(img_path)
                pred_class, prob = prediction(img_path)
                return render_template('show_prediction.html', pred_class=pred_class, prob=prob)
                #return redirect(url_for('show_uploaded_image', filename=filename))
            else:
                return render_template('try_again.html')
    return render_template('upload_image.html')    

@app.route('/uploads/<filename>')
def show_uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    load_model()
    app.run()