import cv2
from matplotlib import pyplot as plt #Is basically a 2-d corrdinate lib.

img = cv2.imread('lena.jpg', -1) #reads the image in BGR format
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

plt.imshow(img) #read the image in RGB format i.e why image looks different.
#plt.xticks([]), plt.yticks([]) # it hides the x-axis and y-axis from the image.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()