import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg', 1)
layer = img.copy()  # copies an image
gp = [layer]  # gaussian pyramid
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

layer = gp[5]
cv.imshow('Upper level Gaussian Pyramid', layer)
lp = [layer]
for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)




# lr1= cv.pyrDown(img) #decreases resolution by 2
# hr2 = cv.pyrUp(lr1) #increases resolution by 2


# cv.imshow('Original image', img)
# cv.imshow('pyrDown 1 image', lr1)
# cv.imshow('pyrUp 2 image', hr2)
cv.waitKey(0)
cv.destroyAllWindows()
