import streamlit as st
from tensorflow.keras.models import load_model 
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from heatmap_utils import heatmap_image


keras_model = '.\saved_models\model_with_preprocess.h5'
heatmap_path = '.\saved_models\\rowing_1213.h5'
default_image_path = '.\default_eight_image.jpg'

model = None # Needed so defining the global variable doesn't raise an issue
def load_trained_model():
    global model
    model = load_model(keras_model)

heatmap_model = None
def load_heatmap_model():
    global heatmap_model
    heatmap_model = load_model(heatmap_path)

def get_uploaded_image():
    uploaded_file = st.file_uploader('Upload an image....', type=['jpg', 'jpeg', 'png'])
        # TODO assert the filetype is an image/safe
        #assert uploaded_file.split('.')[-1] in ['jpg', 'jpeg', 'png'], 'Must be of a certain file type'
    #else:
    #    uploaded_file = default_image_path
    return uploaded_file

def prediction(image):
    img_tensor = _preprocess_img(image)
    model_pred = model.predict(img_tensor)
    pred_class, prob = _map_pred_to_class(model_pred)
    prob = prob*100
    return pred_class, np.round(prob, decimals=3)

def _preprocess_img(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_tensor = tf.keras.preprocessing.image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor = img_tensor/255.
    return img_tensor

def _map_pred_to_class(array):
    l = list(array[0])
    classes = ['Double', 'Eight','Four', 'Pair', 'Quad', 'Single']
    index = l.index(max(l))
    return classes[index], max(l)


def classify_and_show(upload_image):
    image = Image.open(upload_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    with st.spinner('Classifying...'):
        label, prob = prediction(upload_image)
        st.write(f"{label} ({prob}%)")
    st.write('')
    st.write('We can generate a heatmap to highlight what areas of the image the model deemed important')
    if st.button('Generate Heatmap'):
        hm_image = heatmap_image(upload_image, heatmap_model)
        st.image(hm_image, caption='Heatmap Applied to image')


def main():
    st.title('Rowing Image Classification')
    st.write('Try it out for yourself!')
    st.write('Here\'s a default image if you don\'t have any rowing images')
    upload_image = get_uploaded_image()
    if upload_image:
        classify_and_show(upload_image)
    else:
        classify_and_show(default_image_path)

    



if __name__ == '__main__':
    load_trained_model()
    load_heatmap_model()
    main()