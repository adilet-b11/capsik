import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i] #show directories in package cv2 about 'EVENTS'
#print(events)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:#will put circle wherever left click is made
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        cv2.imshow('Image Viewer', img)



#img = np.zeros((512,512,3),np.uint8) #creates black image of 512x512
img = cv2.imread('lena.jpg', 1)
cv2.imshow('Image Viewer', img)
points = []#empty array
cv2.setMouseCallback('Image Viewer', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()