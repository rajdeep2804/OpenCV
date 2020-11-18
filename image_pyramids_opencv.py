#pyramid, or pyramid representaion, is a type of multi-scale signal represntaion in which a signal or an image is subject to repeated smoothing ans subsampling
#2 types of pyramid 1.) Gaussian 2.) Laplacian
#gaussian pyramid : is nothing but repeat filtering and subsampling of an image.
import cv2
import numpy as np
img = cv2.imread("lena.jpg")

lr1 = cv2.pyrDown(img) #lr = lower resolution
lr2 = cv2.pyrDown(lr1)

hr1 = cv2.pyrUp(img) #hr = higher resolution
hr2 = cv2.pyrUp(hr1)

cv2.imshow("Original Image", img)
cv2.imshow("pyrDown one Image", lr1)
cv2.imshow("pyrDown two Image", lr2)
cv2.imshow("pyrUp one Image", hr1)
cv2.imshow("pyrUp two Image", hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()

