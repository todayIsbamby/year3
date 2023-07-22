# -*- coding: utf-8 -*-
"""lab1.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TaxpbW47oAnGPrGyl_pYYf87O_C0TC_t
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("/content/suga-agust-d-bts-hd-wallpaper-preview.jpg")


fig=plt.figure(figsize=(12,12))

b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]
fig.add_subplot(1,4,1)
plt.imshow(img,cmap='gray')
fig.add_subplot(1,4,2)
plt.imshow(b,cmap='gray')
fig.add_subplot(1,4,3)
plt.imshow(g,cmap='gray')
fig.add_subplot(1,4,4)
plt.imshow(r,cmap='gray')

img2=img.copy()
img2=img[:,:,::-1]
r=img2[:,:,0]
g=img2[:,:,1]
b=img2[:,:,2]
fig.add_subplot(2,4,5)
plt.imshow(img2,cmap='gray')
fig.add_subplot(2,4,6)
plt.imshow(r,cmap='gray')
fig.add_subplot(2,4,7)
plt.imshow(g,cmap='gray')
fig.add_subplot(2,4,8)
plt.imshow(b,cmap='gray')

print(img.shape)

imgt=np.transpose(img)
print('Transpose',imgt.shape)
imgm=np.moveaxis(img,2,0)
print('Moveaxis',imgm.shape)
imgr=np.reshape(img,(3,485,728))
print('Reshape',imgr.shape)

fig=plt.figure(figsize=(12,12))

fig.add_subplot(2,4,1)
plt.imshow(b,cmap='gray')
fig.add_subplot(2,4,2)
plt.imshow(imgt[0],cmap='gray')
fig.add_subplot(2,4,3)
plt.imshow(imgm[0],cmap='gray')
fig.add_subplot(2,4,4)
plt.imshow(imgr[0],cmap='gray')