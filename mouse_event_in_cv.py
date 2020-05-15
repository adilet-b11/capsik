import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i] #show directories in package cv2 about 'EVENTS'
#print(events)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:#following condition prints XY coordinates of each pixel when left click is made on picture
        print(x,', ',y) #printing x and y
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+', '+str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5 , (255, 255, 0), 1)
        cv2.imshow('Image Viewer', img)
    if event == cv2.EVENT_RBUTTONDOWN: #following condition prints BGR values of each pixel when right click is made on picture
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(x, ', ', y)  # printing x and y
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green)+', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('Image Viewer', img)

img = cv2.imread('lena.jpg', 1)
cv2.imshow('Image Viewer', img)
cv2.setMouseCallback('Image Viewer', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()