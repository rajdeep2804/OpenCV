import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8) #creating a image through numpy function.
img = cv2.line(img, (0,0), (255,255), (0,0,255),10)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 3)

img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),1)
img = cv2.circle(img, (447,63), 63, (120,120,0), 2)
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img, 'OpenCv', (150,500), font, 2, (255,0,255),2 , cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
