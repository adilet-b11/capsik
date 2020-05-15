import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)

print(img.shape)  # rows, columns, and channels as a tuple
print(img.size)  # total number of pixels in image
print(img.dtype)  # return image datatype
b, g, r = cv2.split(img)


ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# dst=cv2.add(img,img2) #adds img and img2
dst =cv2.addWeighted(img, 0.8, img2, 0.2, 0) #adds img and img2 with corresponding weight (ratio) 0.8 and 0.2

cv2.imshow('Image Viewer', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
