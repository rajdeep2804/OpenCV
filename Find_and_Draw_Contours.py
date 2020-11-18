import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#CONTOURS is a python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("NUMBER OF CONTOURS = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, 0, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()