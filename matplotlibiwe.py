import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Adilet.jpg', 1)
cv.imshow('image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #because matplotlib library only understands RGB, while opencv understand BGR
plt.imshow(img)
#plt.xticks([])  # removes xaxis resolutons
#plt.yticks([])  # removes yaxis resolutons
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
