# -*- coding: utf-8 -*-
"""1b - Finding Contours.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CkP6NhHnsj-CzJByX5mX7q-ZwzGcrkhP
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image of black squares (you can go to this site and choose the one you prefer: https://juliannakunstler.com/vislit_bl_squares.html)
img = cv2.imread('black_squares.png')
plt.imshow(img);

# Also we perform a denoising operation of the image by Bilateral Filter
blurred_img = cv2.GaussianBlur(img, (7, 7), 0)
plt.imshow(blurred_img)

# Find edges using Canny's Edge Detector
edges = cv2.Canny(blurred_img, 30, 50, 3, L2gradient = True)
plt.imshow(edges)

"""### Finding Contours"""

# findContours is a function to find contours in a binary image. Using cv2.RETR_EXTERNAL,
# we give an hierarchy to the contours, meaning that only external contours should be detected
# as a separate contour. CHAIN_APPROX_NONE is the contour approximation method, in this case
# we store all the contour points, without approximating them.

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Now let'see how many contours did we find
print('Number of contours find:', str(len(contours)))

# And draw them. We visualize in green the contours of the objects detected by the algorithm.
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
plt.imshow(img);

"""### For you to try:

1) Try to use *cv2.RETR_LIST* instead of *cv2.RETR_EXTERNAL*... what happens? How many contours are retrieved?

2) If the image you download is not high quality you may obtain the double of the contours actually present in the image...to solve this problem you need to denoise the image even more or perform a contour selection.
"""