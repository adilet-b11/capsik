import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 640) #setting width
#cap.set(4, 480) #setting height
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():
    ret, frame = cap.read()
    if ret==1:
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        datet = str(datetime.datetime.now()) #adding time to video
        text = 'Width: '+str(width) +' Height: '+ str(height)
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, text, (0,240), font, 1, (0,255,0), 2, cv2.LINE_AA ) 
        frame = cv2.putText(frame, datet, (0, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()