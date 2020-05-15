import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # compares all pixels of img with 127 value.
# Those which are less are assigned to 0, which are higher assigned to 255
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  # inverse of Binary
_, th3 = cv.threshold(img, 20, 255, cv.THRESH_TRUNC)  # which is less than 20 doesnt chane anything, which is
# higher than 20 makes 20
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # compares every pixel by 127 and which is less makes them 0
# which is higher doesnt change
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
# cv.imshow('Image', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)
# rather than the code above we can use matplotlib library which is more convenient
titles =['Original image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_inv']
images = [img, th1, th2, th3, th4 ,th5]

for i in range(6):
    plt.subplot(2,3, i+1,), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
