from matplotlib import pyplot as plt
import cv2
import numpy as np


img = cv2.imread('Adilet.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
a = img[29,309]
b = img[210,309]
print(a)
print(b)



palette = []
for i in range(0, 181, 1):
    palette.append(img[30 + i, 309])

temperature_range  = np.linspace(36.3, 26, 181)
h = img.shape[0]
w = img.shape[1]
print(palette[0])
print(img[5,5])


for y in range(0, h):
    for x in range(0, w):
        check = True;
        checks = img[y, x] == palette[0]
        print(checks)
        for c in checks:
            check &= c
        if check:
            print('Temperature ' + str(temperature_range[0]))





#plt.imshow(img)
#plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
