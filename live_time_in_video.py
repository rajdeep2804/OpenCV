import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#print(cap.get(3))
#print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        total = str(text) + str(datet)
        frame = cv2.putText(frame, total, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()