import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)  # homogenous filtering blurring
blur = cv.blur(img, (5, 5))  # blurring
gblur = cv.GaussianBlur(img, (5, 5), 0)  # better blur imho, removes high grequency noiz
median = cv.medianBlur(img, 5)  # Kernel size must be odd except '1', removes salt and pepper noise
bilateral_filter = cv.bilateralFilter(img, 9, 75, 75) # edges of image are preserved, but inner parts are blurred :)

titles = ['images', '2D Convolution', 'blur', 'Gaussian blur', 'median', 'bilateral_filter']
images = [img, dst, blur, gblur, median, bilateral_filter]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
