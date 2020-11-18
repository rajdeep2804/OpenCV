import cv2 #as in 1-d signals images also can be filtered with various low pass filters, high pass filters etc.
import numpy as np #lpf helps in removing noises, blurring the images, hpf helps in finding edges in the images.
from matplotlib import pyplot as plt #gaussian fliter is nothing but using differnt-weight-kernel, in both x and y direction.
img = cv2.imread('lena.jpg') #median filter is something that replace each pixel's, this method is great when dealing with "salt and pepper noise".
img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5, )
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D convolution', 'blur', 'gblur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range (6) :
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()