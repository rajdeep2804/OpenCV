#the canny edge detection is an edge detection operator that uses a multi-stage algorithm to detect
#a wide range of edges in images. it was developed by john f canny in 1986
#the canny edge detection algorithm is composed of 5 steps:
# 1.) noise reduction
# 2.) gradient calculation
# 3.) non-maximum suppression
# 4.) double threshold
# 5.) edge tracking by Hysteresis

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("lena.jpg", 0 )
canny = cv2.Canny(img, 100, 200, )
titles = ["image", "canny"]
image = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()