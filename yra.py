import cv2 as cv
from matplotlib import pyplot as plt

adilet = cv.imread('IMG_4896.JPG', 1)
yra = cv.imread('yra.jpg', 1)
print(yra.shape)
adilet = cv.resize(adilet, (612,816), interpolation = cv.INTER_AREA)
yra = cv.resize(yra, (612,344), interpolation = cv.INTER_AREA)

gray=cv.cvtColor(yra, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3, 3), 0)
_, thresh = cv.threshold(blur, 230, 255, cv.THRESH_BINARY)
dilated = cv.dilate(thresh, None, iterations=3)
contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(yra, contours, -1, (0, 0, 255), 1)
cv.imshow('asd', adilet)
cv.imshow('123', yra)
cv.waitKey(0)
cv.destroyAllWindows()



"""titles = [] #plotting the results
images = [adilet]

for i in range(1):
    plt.subplot(1, 1, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()"""