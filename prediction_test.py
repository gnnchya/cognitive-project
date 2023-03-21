import numpy as np
from keras.utils import load_img, img_to_array
import tensorflow as tf
import os

# Load the model
model = tf.saved_model.load('/Users/fluke/Documents/GitHub/cognitive-project/model3')

# Make the prediction
def pred(x):
    preds = model(x)

    # Get the predicted class label
    class_idx = np.argmax(preds[0])
    class_label = {'class_0': 0, 'class_1': 1, 'class_2': 2, 'class_3': 3, 'class_4': 4}
    for key, value in class_label.items():
        if value == class_idx:
            print('Predicted class:', key)

# Load the image

# specify the directory path
directory = '/Users/fluke/Documents/GitHub/cognitive-project/example'

# use os.listdir() to get a list of all files in the directory
files = os.listdir(directory)

# print the list of files
for i in files:
    img_path = '/Users/fluke/Documents/GitHub/cognitive-project/example/'+i
    img = load_img(img_path, target_size=(640,640))

    # Preprocess the image
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0
    pred(x)

