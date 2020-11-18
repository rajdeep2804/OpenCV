import numpy as np
import cv2

img = cv2.imread('shapes.png')
imGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting the image into grayscale image.

_, thrash = cv2.threshold(imGrey, 240, 255, cv2.THRESH_BINARY) #finging the threshold
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #finging the contours

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()