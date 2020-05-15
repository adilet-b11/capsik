import cv2 as cv
import numpy as np


def nothing(x):
    print(x)



cv.namedWindow('image')  # create a window with name 'image'
cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while (True):
    img = cv.imread('lena.jpg', 1)
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4 , (0, 0, 0))

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    elif s == 1:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image', img)
cv.destroyAllWindows()
