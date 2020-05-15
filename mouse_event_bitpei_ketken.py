import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i] #show directories in package cv2 about 'EVENTS'
#print(events)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:#will take the colour of one pixel and shows it on other image
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorimage = np.zeros((512,512,3), np.uint8)

        mycolorimage[:] = [blue, green,red]

        cv2.imshow('color', mycolorimage)



#img = np.zeros((512,512,3),np.uint8) #creates black image of 512x512
img = cv2.imread('lena.jpg', 1)
cv2.imshow('Image Viewer', img)
points = []#empty array
cv2.setMouseCallback('Image Viewer', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()