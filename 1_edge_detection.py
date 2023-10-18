# -*- coding: utf-8 -*-
"""1 - Edge Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_rVXCxESTs42yUWKMX8oBeBPGW2zq_Ij
"""

import cv2
import matplotlib.pyplot as plt

# Read the image:
img = cv2.imread('dancing spider.jpg')

# Apply Canny Edge Detector:
edges = cv2.Canny(img, 100, 200, 3, L2gradient = True)

# Visualize the image:
plt.figure()
plt.title('Dancing Spider')
plt.imsave('dancing spider - Canny.jpg', edges, cmap = 'gray', format = 'jpg')
plt.imshow(edges, cmap = 'gray')
plt.show()

"""For you to try:

1) When calling the Canny operator, the paramters 100 and 200 refer to the lower and higher thresholds of the Canny isteresis (so in practice it handles how many edges we want to perform). Try to change those values and show the corresponding image, trying to notice the differences.

"""