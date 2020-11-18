import numpy as np
import cv2
#events = [i for i in dir(cv2) if 'EVENT' in i] # for printing all the events inside the open cv library.
#print(events)
def click_event(event, x, y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

       cv2.circle(img, (x,y), 3, (0,0,255), -1)
       points.append((x,y)) # whenever we are going to click it will append all those points.
       if len(points) >=2:
           cv2.line(img, points[-1], points[-2], (255,0,0), 5)
       cv2.imshow('image', img)

#img = np.zeros((512, 512,3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image', click_event) #window name should be same i.e 'image' is the first parameter and 2nd papameter is the callback function.(click_event)
cv2.waitKey()
cv2.destroyAllWindows()







