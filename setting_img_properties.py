import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()): # or we can take argument to be 0
    ret, frame = cap.read() #ret argument is bol t/f if ret is true it will read video.
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #In this cv2.color_bgr2gray we are converting colored image o gray.
        cv2.imshow('frame',gray) # frame arument is name of the video and gray argument it video capture
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()