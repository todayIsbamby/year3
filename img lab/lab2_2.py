# -*- coding: utf-8 -*-
"""Lab2_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rTNoI00c8YVSCbH03ouAhB7mj13NC9Rd
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img=cv2.imread("/content/pic3.jpg")

img=cv2.resize(img,(400,400))

# his_r = cv2.calcHist(img2[:,:,2],[0],None,[256],[0,256])
# his_g = cv2.calcHist(img2[:,:,1],[0],None,[256],[0,256])
# his_b = cv2.calcHist(img2[:,:,0],[0],None,[256],[0,256])
# plt.plot(his_r, color='r')
# plt.plot(his_g, color='g')
# plt.plot(his_b, color='b')
# plt.title('Image Histogram')
# plt.show()

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = np.zeros((400,400,3))
r = cv2.equalizeHist(img_rgb[:,:,0])
g = cv2.equalizeHist(img_rgb[:,:,1])
b = cv2.equalizeHist(img_rgb[:,:,2])

plt.figure()
fig = plt.figure(figsize=(20,20))

fig.add_subplot(2,2,1)
plt.imshow(img_rgb)

fig.add_subplot(2,2,2)
his_r = cv2.calcHist(img_rgb[:,:,0],[0],None,[256],[0,256])
his_g = cv2.calcHist(img_rgb[:,:,1],[0],None,[256],[0,256])
his_b = cv2.calcHist(img_rgb[:,:,2],[0],None,[256],[0,256])
plt.plot(his_r, color='r')
plt.plot(his_g, color='g')
plt.plot(his_b, color='b')
plt.title('his original')

fig.add_subplot(2,2,3)
img2 = cv2.merge((r,g,b))
plt.imshow(img2)

fig.add_subplot(2,2,4)
his_r = cv2.calcHist([img2[:,:,0]],[0],None,[256],[0,256])
his_g = cv2.calcHist([img2[:,:,1]],[0],None,[256],[0,256])
his_b = cv2.calcHist([img2[:,:,2]],[0],None,[256],[0,256])
plt.plot(his_r, color='r')
plt.plot(his_g, color='g')
plt.plot(his_b, color='b')
plt.title('his eq')


fig.tight_layout()
plt.show()


# cv2_imshow(img2)