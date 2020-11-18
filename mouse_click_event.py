import numpy as np
import cv2
#events = [i for i in dir(cv2) if 'EVENT' in i] # for printing all the events inside the open cv library.
#print(events)
def click_event(event, x, y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img) # will show this text on the image

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 0), 2)
        cv2.imshow('image', img)  # will show this text on the image


#img = np.zeros((512, 512,3), np.uint8)
img = cv2.imread('lena.jpg') 
cv2.imshow('image',img)
cv2.setMouseCallback('image', click_event) #window name should be same i.e 'image' is the first parameter and 2nd papameter is the callback function.(click_event)
cv2.waitKey()
cv2.destroyAllWindows()







