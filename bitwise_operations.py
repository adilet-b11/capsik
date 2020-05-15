import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)  # creating a black image with 250 rows and 500 columns
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)  # filled white rectangle starting
# at column = 200, row = 0, ending at column = 300 and row =100
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)
# bitAnd = cv2.bitwise_and(img2, img1)
# bitOr = cv2.bitwise_or(img2,img1)
# bitXor = cv2.bitwise_xor(img2, img1)
bitNot = cv2.bitwise_not(img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
# cv2.imshow('bitAnd', bitAnd) #multiplication
# cv2.imshow('bitOr', bitOr) #summation
# cv2.imshow('bitXor', bitXor) #if same return 0, if diverse gives 1
cv2.imshow('bitNot', bitNot) #inverts 1 to 0, 0 to 1


cv2.waitKey(0)
cv2.destroyAllWindows()
