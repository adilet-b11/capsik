import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', 0)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv.dilate(mask, kernel, iterations=2)  # removing dots from inside the circle

erosion = cv.erode(mask, kernel, iterations=2)  # decreasing the size of circle

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, )  # erosion then dilation is done

closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, )  # dilation then erosion is done

mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel, )

th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, )

titles = ['images', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()