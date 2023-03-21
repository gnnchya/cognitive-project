import tensorflow as tf

# Load the Keras model
keras_model = tf.keras.models.load_model('/Users/gnnchya/Documents/cognitive-keras/many.h5')

# Convert the Keras model to a SavedModel format
tf.saved_model.save(keras_model, '/Users/gnnchya/Documents/cognitive-keras/saved_model_many/')