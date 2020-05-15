import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', 0)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)  # the second argument is float datatype
laplacian = np.uint8(np.absolute(laplacian))  # found laplacian edge detection

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)  # '1' is order of derivative x, '0' is for y
sobelX = np.uint8(np.absolute(sobelX))  # sobelX is vertical

sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))  # sobelY is horizontal

sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['images', 'Laplacian', 'sobelX', 'sobelY','sobelCombined']
images = [img, laplacian, sobelX, sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
