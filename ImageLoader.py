import os
from PIL import Image
import numpy as np
def loadImages():
    labels = ['brik', 'salade mechouia', 'ojja', 'couscous', 'lablebi', 'mloukhiya']
    testDirectory = r'C:\Users\slimw\Downloads\Test'
    trainDirectory = r'C:\Users\slimw\Downloads\Train'
    X_train = np.array([np.asarray(Image.open(r'C:\Users\slimw\Downloads\briktrain1.jpg'))])
    X_test = np.array([np.asarray(Image.open(r'C:\Users\slimw\Downloads\briktest1.jpg'))])
    y_train = np.array(np.asarray([[0]]))
    y_test = np.array(np.asarray([[0]]))
    for filename in os.listdir(trainDirectory):
        X_train = np.append(X_train, [np.asarray(Image.open(trainDirectory + '\\' + filename))], axis=0)
        if "brik" in filename:
            y_train = np.append(y_train, [[labels.index("brik")]], axis=0)
        elif "salade" in filename:
            y_train = np.append(y_train, [[labels.index("salade mechouia")]], axis=0)
        elif "ojja" in filename:
            y_train = np.append(y_train, [[labels.index("ojja")]], axis=0)
        elif "couscous" in filename:
            y_train = np.append(y_train, [[labels.index("couscous")]], axis=0)
        elif "lablabi" in filename:
            y_train = np.append(y_train, [[labels.index("lablebi")]], axis=0)
        elif "mloukhiya" in filename:
            y_train = np.append(y_train, [[labels.index("mloukhiya")]], axis=0)

    for filename in os.listdir(testDirectory):
        X_test = np.append(X_test, [np.asarray(Image.open(testDirectory + '\\' + filename))], axis=0)
        if "brik" in filename:
            y_test = np.append(y_test, [[labels.index("brik")]], axis=0)
        elif "salade" in filename:
            y_test = np.append(y_test, [[labels.index("salade mechouia")]], axis=0)
        elif "ojja" in filename:
            y_test = np.append(y_test, [[labels.index("ojja")]], axis=0)
        elif "couscous" in filename:
            y_test = np.append(y_test, [[labels.index("couscous")]], axis=0)
        elif "lablabi" in filename:
            y_test = np.append(y_test, [[labels.index("lablebi")]], axis=0)
        elif "mloukhiya" in filename:
            y_test = np.append(y_test, [[labels.index("mloukhiya")]], axis=0)
    return X_train, X_test, y_train, y_test
