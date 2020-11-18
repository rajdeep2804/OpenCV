# an image gradient is a directional change in the intensity or color in an image.
#for eg we use image gradient to find the edges inside the image.
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # cv_64f is the datatype which we are going to use it is a 64 bit float, due to the negative slop induced by transforming the image by white to black.
lap = np.uint8(np.absolute(lap)) #we are going to take the aboulte value of laplacian image tranformation converting the value back to the unsigned 8 bit integar value.

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
edges = cv2.Canny(img, 100, 200)

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]
for i in range(6) :
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()