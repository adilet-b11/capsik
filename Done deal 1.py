import cv2 #importing libraries
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0) #uploading the video from a webcam

while cap.isOpened(): #making sure the video is present
    ret, frame = cap.read() #assigning an each frame into variable
    originaliwe = frame.copy() #making the copy of each frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting from BGR to RGB
    if ret==1: #making sure the video is present
        gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #converting the frame from RGB to grayscale
        blur = cv2.GaussianBlur(gray, (5, 5), 0) #blurring the frame
        ret, thresh = cv2.threshold(blur, 250, 255, cv2.THRESH_BINARY) #binary thresholding
        dilated = cv2.dilate(thresh, None, iterations=3) #removing the noise
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #obtaining the contours of dialted frame
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour) #calculating the area of contour
            if bool(cv2.contourArea(contour) < 3000) & bool(cv2.contourArea(contour) > 300): #checking the area of contours
                cv2.drawContours(frame, contour, -1, (255, 0, 0), 3) #drawing contours
                cv2.putText(frame, "Fault", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3) #putting a red text near the fault
                print(cv2.contourArea(contour))
        titles = ['Original frame', 'Gray', 'Blur', 'Thresh','Dilation', 'Resultant frame'] #plotting the results
        images = [originaliwe, gray, blur, thresh, dilated, frame]

        for i in range(6):
            plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i]) #removing x and y labels
            plt.xticks([]), plt.yticks([])

        plt.show()
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release() #deleting the video
cv2.destroyAllWindows()