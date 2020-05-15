import cv2
import numpy as np
#img = cv2.imread('lena.jpg', 1)

img = np.zeros([512,1000, 3], np.uint8)

img=cv2.line(img, (0,0), (255,255), (255, 30, 251), 5 )
img=cv2.arrowedLine(img, (0,255), (255,255), (0, 250, 0), 5 )
img = cv2.rectangle(img, (255,255), (500,500), (255,0,0), -1)
img = cv2.circle(img, (100,350), 63, (0,0,255), 5)
font =cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'asdasd', (10,500), font, 4, (255,255,255), 5, cv2.LINE_AA)
cv2.imshow('window_name',img)
cv2.waitKey(0)
cv2.destroyAllWindows()