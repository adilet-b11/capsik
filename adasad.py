import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_kek = cv.imread('Zhumazhenis.jpg') #uploading an image
print(img_kek.shape)
img_kek_result = img_kek[30:213, 30:278]
#print(img_kek[5:5, 100:50])
cv.imshow('asd',img_kek_result)
cv.waitKey(0)
cv.destroyAllWindows()