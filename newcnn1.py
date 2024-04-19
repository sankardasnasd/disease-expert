# # coding: utf-8

# # In[ ]:
# import os

# import tensorflow as tf
# # sess = tf.Session()
# import keras
# from keras.engine.saving import load_model
# from keras.models import Sequential
# from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
# from keras.layers import Dense, Activation, Dropout, Flatten

# from keras.preprocessing import image
# from keras.preprocessing.image import ImageDataGenerator

# import numpy as np

# #------------------------------
# # sess = tf.Session()
# # keras.backend.set_session(sess)
# #------------------------------
# #variables
# num_classes =38
# batch_size = 40
# epochs = 50
# #------------------------------

# import os, cv2, keras
# import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# from keras.engine.saving import load_model
# # manipulate with numpy,load with panda
# import numpy as np
# # import pandas as pd

# # data visualization
# import cv2
# import matplotlib
# import matplotlib.pyplot as plt
# # import seaborn as sns

# # get_ipython().run_line_magic('matplotlib', 'inline')


# # Data Import
# def read_dataset(): ##details image access
#     data_list = []
#     label_list = []
#     i=0
#     my_list = os.listdir(r'static\\dataset')
#     for pa in my_list:

#         print(pa,"==================",i)
#         for root, dirs, files in os.walk(r'static\\dataset\\' + pa):

#          for f in files:
#             file_path = os.path.join(r'static\\dataset\\'+pa, f)
#             print(file_path)
#             img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
#             res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
#             data_list.append(res)
#             # label = dirPath.split('/')[-1]
#             label = i
#             label_list.append(label)
#         i=i+1

#     return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

# def read_dataset1(path):
#     data_list = []
#     label_list = []

#     file_path = os.path.join(path)
#     img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
#     res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
#     data_list.append(res)
#     # label = dirPath.split('/')[-1]

#             # label_list.remove("./training")
#     return (np.asarray(data_list, dtype=np.float32))

# from sklearn.model_selection import train_test_split
# # load dataset
# x_dataset, y_dataset = read_dataset()
# X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.5, random_state=0)

# y_train1=[]
# for i in y_train:
#     emotion = keras.utils.to_categorical(i, num_classes)
#     print(i,emotion)
#     y_train1.append(emotion)

# y_train=y_train1
# x_train = np.array(X_train, 'float32')
# y_train = np.array(y_train, 'float32')
# x_test = np.array(X_test, 'float32')
# y_test = np.array(y_test, 'float32')

# x_train /= 255  # normalize inputs between [0, 1]
# x_test /= 255
# print("x_train.shape",x_train.shape)
# x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
# x_train = x_train.astype('float32')
# x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
# x_test = x_test.astype('float32')

# print(x_train.shape[0], 'train samples')
# print(x_test.shape[0], 'test samples')
# # ------------------------------
# # construct CNN structure

# model = Sequential()

# # 1st convolution layer
# model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
# model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))

# # 2nd convolution layer
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

# # 3rd convolution layer
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

# model.add(Flatten())

# # fully connected neural networks
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))

# model.add(Dense(num_classes, activation='softmax'))
# # ------------------------------
# # batch process

# print(x_train.shape)

# gen = ImageDataGenerator()
# train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

# # ------------------------------

# model.compile(loss='categorical_crossentropy'
#               , optimizer=keras.optimizers.Adam()
#               , metrics=['accuracy']
#               )

# # ------------------------------

# if not os.path.exists("model1.h5"):

#     model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
#     model.save("model1.h5")  # train for randomly selected one
# else:
#     model = load_model("model1.h5")  # load weights
# from sklearn.metrics import confusion_matrix
# yp=model.predict_classes(x_test,verbose=0)
# cf=confusion_matrix(y_test,yp)
# print(cf)

# from sklearn.metrics import accuracy_score
# acc=accuracy_score(y_test, yp)
# print(acc)

# # def predictcnn(fn):
# #     dataset=read_dataset1(fn)
# #     (mnist_row, mnist_col, mnist_color) = 48, 48, 1

# #     dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
# #     mo = load_model("mode1.h5")

# #     # predict probabilities for test set

# #     yhat_classes = mo.predict_classes(dataset, verbose=0)
# #     return yhat_classes
# #
# #     print(yhat_classes)

# #predict(r"D:\vehicle classification with deep learning\src\semi-semitrailer-truck-tractor-highway.jpg")



import os
import cv2
import numpy as np
import tensorflow as tf
# from tensorflow.keras.models import Sequential, load_model
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, Dense, Dropout, Flatten
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


# import os

# import tensorflow as tf
# # sess = tf.Session()
import keras
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np


# Function to read the dataset
def read_dataset():
    data_list = []
    label_list = []
    num_classes = 38

    for i, class_folder in enumerate(os.listdir(r'static\\test')):
        for filename in os.listdir(os.path.join(r'static\\test', class_folder)):
            file_path = os.path.join(r'static\\test', class_folder, filename)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            resized_img = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            data_list.append(resized_img)
            label_list.append(i)

    return np.asarray(data_list, dtype=np.float32), to_categorical(label_list, num_classes)

# Load and preprocess the dataset
x_dataset, y_dataset = read_dataset()
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.5, random_state=0)

x_train = X_train.astype('float32') / 255
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
y_train = np.array(y_train, 'float32')

x_test = X_test.astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
y_test = np.array(y_test, 'float32')

# Build the CNN model
model = Sequential()
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(38, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, batch_size=40, epochs=50)

# Evaluate the model
y_pred = model.predict_classes(x_test)
cf = confusion_matrix(np.argmax(y_test, axis=1), y_pred)
print("Confusion Matrix:\n", cf)
acc = accuracy_score(np.argmax(y_test, axis=1), y_pred)
print("Accuracy:", acc)

# Save the trained model
model.save("model6.h5")
