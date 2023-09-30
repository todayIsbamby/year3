# -*- coding: utf-8 -*-
"""5.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m8MTF4SAglDhUMKamUfdJ9azQyQHMj-7
"""

!pip install tensorflow==2.12

import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from keras import Model, Input
import keras.utils as image
from keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, UpSampling2D
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import optimizers

from tensorflow.keras.datasets import fashion_mnist

from sklearn.model_selection import train_test_split
from google.colab.patches import cv2_imshow

# Load the image
# img = cv2.imread("/content/drive/MyDrive/datasetimgs/Grid_Image.jpg")
img = cv2.imread("/content/drive/MyDrive/datasetimgs/suga-agust-d-bts-hd-wallpaper-preview (2).jpg")
# Define resize factor
# Reduce_factors = [2, 4, 5, 7, 8, 10, 15] # อย่างน้อย 3 ค่า
Reduce_factors=[2,5,8]
Scale_factors = [1 / factor for factor in Reduce_factors]
# Define interpolation method
inter_methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA]
tt=["INTER_NEAREST","INTER_LINEAR","INTER_CUBIC","INTER_AREA"]

print(Scale_factors)

# Create subplots to display the results
plt.figure(figsize=(15, 9))

for i, scale_factor in enumerate(Scale_factors):

    for j, inter_method in enumerate(inter_methods):

        #calculate new dimension for resize
        new_width = int(img.shape[1] * scale_factor)
        new_height = int(img.shape[0] * scale_factor)

        # Resize the image using each scale factor and interpolation method
        resized_image = cv2.resize(img, (new_width,new_height), fx=scale_factor, fy=scale_factor, interpolation=inter_method)
        plt.subplot(3, 4, (j + 1)  + (i *len(inter_methods)))
        plt.title(tt[j])
        plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))


# Adjust subplot layout
plt.tight_layout()
plt.show()