from PIL import Image
import numpy as np
from keras.models import load_model
from keras import utils
from ImageLoader import loadImages
X_train, X_test, y_train, y_test = loadImages()
new_X_train = X_train.astype('float32')
new_X_test = X_test.astype('float32')
new_X_train /= 255
new_X_test /= 255
new_y_train = utils.np_utils.to_categorical(y_train)
new_y_test = utils.to_categorical(y_test)
labels=['brik', 'salade mechouia', 'ojja', 'couscous', 'lablebi', 'mloukhiya']
model1 = load_model('Trained Model_SeeFood_new.h5')
model2 = load_model('New_Model.h5')
input_path = r'C:\Users\slimw\Downloads\lablebifortest1.jpg'
input_image = Image.open(input_path)
input_image = input_image.resize((128, 128), resample=Image.LANCZOS)
image_array = np.array(input_image)
image_array = image_array.astype('float32')
image_array /= 255
image_array = image_array.reshape(1, 128, 128, 3)
answer2 = model2.predict(image_array)
print('The image is : '+labels[np.argmax(answer2)])
print(answer2)
print(model2.evaluate(new_X_test, new_y_test, verbose=0))