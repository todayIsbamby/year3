# -*- coding: utf-8 -*-
"""lab6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Bb1lMVAxxazb3nPAhIHIaXSvjDqeK5G
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator



#Load base model
base_model=MobileNet(weights='imagenet',include_top=False, input_shape=(224, 224, 3))

# Add new layers
x=base_model.output
x = GlobalAveragePooling2D()(x)

# เพิ่มชั้น Dense 3 Layers: L1 (1024 Nodes), L2 (1024 Nodes), L3 (512 Nodes
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)

# เพิ่มชั้น Dense 1 Layer (L4 (3 Nodes)) โดยใช้ Activation 'Softmax' สำหรับการสรุปผลลัพธ์ 3 classes
pred = Dense(3, activation='softmax')(x)

# Assign transfer base model + new layers to model
model=Model(inputs=base_model.input,outputs=pred)
model.summary()


print()

# Assign Trainable layers and freeze layer -> ลองเปลี่ยน ช่วง layer ในการ trainable True/False 3 ค่า เพื่อดูความแตกต่างของผลลัพธ์ที่ได้
for layer in model.layers[:86]:
   layer.trainable=False #Freeze base model
for layer in model.layers[86:]:
   layer.trainable=True #Unfreeze new added denses
for i, layer in enumerate(base_model.layers): # ตรวจสอบค่า trainable ของแต่ละชั้น
    print(i, layer.name)

# Create DataGeneartor Object
rotation_range = 90
width_shift_range = 0.5
height_shift_range = 0.5
shear_range = 0.2
zoom_range = 0.5
horizontal_flip = True

datagen=ImageDataGenerator( rotation_range=rotation_range, zoom_range=zoom_range,width_shift_range=width_shift_range, height_shift_range=height_shift_range,
                            shear_range=shear_range,horizontal_flip=horizontal_flip, preprocessing_function=preprocess_input,fill_mode="nearest")

from google.colab import drive
drive.mount('/content/drive')
# Create Train Image generator
batch_size=16
seed_value=42
train_generator=datagen.flow_from_directory('/content/drive/MyDrive/datasetimgs/Ship/Train', # this is where you specify the path to the main data folder

                                            target_size=(224,224), color_mode='rgb',
                                            batch_size=batch_size,
                                            class_mode='categorical', seed = seed_value,
                                            shuffle=True)

# Create Validation Image generator

val_generator=datagen.flow_from_directory('/content/drive/MyDrive/datasetimgs/Ship/Validate', # this is where you specify the path to the main data folder

                                          target_size=(224,224), color_mode='rgb',
                                          batch_size=batch_size,
                                          class_mode='categorical', seed = seed_value,
                                          shuffle=True)

plt.figure(figsize=(15, 9))

# Get and display multiple batches of training images in a 4x4 grid
for i in range(4):
    # Get a batch of training images
    batch = train_generator.next()
    Img_train_batch = batch[0]  # Extract the batch of images

    # Rescale the pixel values from [-1.0, 1.0] to [0.0, 1.0]
    Img_train_batch = (Img_train_batch + 1.0) / 2.0

    # Plot the images in the current row of the grid
    for j in range(4):
        plt.subplot(4, 4, (i *4) + (j + 1))  # 4x4 grid, ith row, jth column
        plt.imshow(Img_train_batch[j])  # Display the jth image from the batch
        plt.title('Training Image')

plt.figure(figsize=(15, 9))
# Rescale the pixel values from [-1.0, 1.0] to [0.0, 1.0]
for i in range(4):
      batch = val_generator.next()
      Img_val = batch[0]  # Extract the batch of images
      Img_val = (Img_val + 1.0) / 2.0
      for j in range(4):
            # Visualize the first image from the batch
            plt.subplot(4, 4, (i *4) + (j + 1))
            plt.imshow(Img_val[j])
# Show the plot
plt.tight_layout()  # Ensure subplots don't overlap
plt.show()

# Create Optimizer
opts = Adam(learning_rate = 0.0001)
model.compile(loss='categorical_crossentropy',optimizer=opts,metrics=['accuracy'])

# Define training Generator Parameter
EP=100 # Number of Iterations
step_size_train=train_generator.n//train_generator.batch_size
step_size_val = val_generator.n//val_generator.batch_size
# check step_size_Train = step_size_val -> if not, adjust batch_size to make it equal

history=model.fit_generator(generator=train_generator,
            steps_per_epoch=step_size_train,
            validation_data = val_generator,
            validation_steps = step_size_val,
            epochs=EP,
            verbose = 1)

N = range(1, EP+1)

# View Accuracy (Training, Validation)
plt.plot(N, history.history["accuracy"], label="Train_acc")
plt.plot(N, history.history["val_accuracy"], label="Validate_acc")

# View Loss (Training, Validation)
plt.plot(N, history.history['loss'], label="Train_loss")
plt.plot(N, history.history['val_loss'], label="Validate_loss")

plt.legend()  # Add legend to the plot
plt.show()  # Display the plot

#6.3

# Initial test generator

test_generator = datagen.flow_from_directory(
              '/content/drive/MyDrive/datasetimgs/Ship/Test',
              class_mode="categorical",
              target_size=(224, 224), color_mode="rgb",
              shuffle=False,
              batch_size=1)

#Get class id for y_real_class
y_true = test_generator.classes

#predict images according to test_generator # number of real class
preds = model.predict_generator(test_generator)
print(preds.shape)
print(preds)

y_pred = np.argmax(preds,axis=1)
print(test_generator.classes)
print(y_pred)

# Calculate confusion matrix, classification report between y_true and df_class
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred))