import tensorflow as tf
from keras.layers import Dense, Input, GlobalAveragePooling2D, Dropout, Reshape
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator

def create_model(num_classes, input_shape=(640, 640, 3)):
    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape, include_top=False)
    base_model.trainable = False

    inputs = Input(shape=input_shape)
    x = base_model(inputs, training=False)
    x = GlobalAveragePooling2D()(x)    
    x = Dropout(0.2)(x)
    x = Dense(125)(x)
    outputs = Dense(num_classes, activation='softmax')(x)

    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model



# Set up data generators
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '/Users/gnnchya/Documents/cognitive-keras/data_temp/train',
        target_size=(640, 640),
        batch_size=32,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        '/Users/gnnchya/Documents/cognitive-keras/data_temp/test',
        target_size=(640, 640),
        batch_size=32,
        class_mode='categorical')

# Create the model
model = create_model(num_classes=5)
print('here')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print('here2')
# Train the model
history = model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Save the model
tf.saved_model.save(model, '/Users/gnnchya/Documents/cognitive-keras/model1/')



#python -m tf2onnx.convert --saved-model /Users/gnnchya/Documents/cognitive-keras/model2 --output model.onnx
