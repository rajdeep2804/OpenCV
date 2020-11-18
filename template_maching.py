#Template maching is a method of searching and finding the location of a template image inside a larger image.
# in open cv there is method called match template.
import cv2
import numpy as np

img = cv2.imread("one_plus_2.jpg")

grey_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
template = cv2.imread("gallery_test.JPG",0 )
w, h = template.shape[::-1] #-1 means we want the column and rows values in the reverse order.
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.75;
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]): #if there are multiple number of matched templates,then for loop will be required to templates we need to itrate
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] +h),(0,0,255), 2)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()