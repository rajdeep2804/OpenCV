#histogram is a graph or a plot which gives you an overall idea about intensity distribusion of an image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#plt.hist(img.ravel(), 256, [0, 256])
#b, g, r = cv.split(img)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

#cv.imshow("img", img)
#cv.imshow("b", b)
#cv.imshow("g", g)
#cv.imshow("r", r)


#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])

plt.show()

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()