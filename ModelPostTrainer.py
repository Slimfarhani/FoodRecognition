from keras.utils import np_utils
import  ImageLoader as loader
from PIL import Image
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.constraints import maxnorm
from keras.models import load_model
labels=['brik', 'salade mechouia', 'ojja', 'couscous', 'lablebi', 'mloukhiya']
model = load_model('New_Model.h5')
input_path = r'C:\Users\slimw\Downloads\couscousfortest1.jpg'
input_image = Image.open(input_path)
input_image = input_image.resize((128, 128), resample=Image.LANCZOS)
image_array = np.array(input_image)
image_array = image_array.astype('float32')
image_array /= 255
image_array = image_array.reshape(1, 128, 128, 3)
y_train = np.array(np.asarray([[labels.index('couscous')]]))
new_y_train = np_utils.to_categorical(y_train, 6)
print(new_y_train.shape)
print(image_array.shape)
model.compile(optimizer = 'Adam' , loss = "categorical_crossentropy", metrics=["accuracy"])
model.fit(image_array, new_y_train, epochs=3, batch_size=1)
import h5py
model.save('New_Model.h5')