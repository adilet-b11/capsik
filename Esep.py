import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    print(x)


cv.namedWindow('trackbar')  # create a window with name 'image'
cv.createTrackbar('TH1', 'trackbar', 0, 1000, nothing)
cv.createTrackbar('TH2', 'trackbar', 0, 1000, nothing)

img = cv.imread('asdpur.jpg', 1)
z = cv.rectangle(img, (417, 297), (540, 335), (255, 255, 255), -1)
while (True):

    th1 = cv.getTrackbarPos('TH1', 'trackbar')
    th2 = cv.getTrackbarPos('TH2', 'trackbar')
    canny = cv.Canny(z, threshold1=th1, threshold2=th2)
    cv.imshow('image', z)
    cv.imshow('canny', canny)
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()
