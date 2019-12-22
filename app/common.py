import tensorflow as tf
import numpy as np

def _preprocess_img(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_tensor = tf.keras.preprocessing.image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor = img_tensor/255.
    return img_tensor

def _map_pred_to_class(array):
    l = list(array[0])
    classes = ['Doubles', 'Eights','Fours', 'Pairs', 'Quads', 'Singles']
    index = l.index(max(l))
    return classes[index], max(l)