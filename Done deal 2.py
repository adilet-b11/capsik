import cv2

cap = cv2.VideoCapture(0)

print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()
    if ret==1:
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, thresh = cv2.threshold(blur, 250, 255, cv2.THRESH_BINARY)
        #cv2.imshow('thresh', thresh)
        dilated = cv2.dilate(thresh, None, iterations=3)
        #cv2.imshow('dilation', dilated)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if bool(cv2.contourArea(contour) < 3000) & \
                    bool(cv2.contourArea(contour) > 300):
                cv2.drawContours(frame, contour, -1, (0, 0, 255), 3)
                cv2.putText(frame, "Fault", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 3)
                print(cv2.contourArea(contour))
        #print('Number of contours = ' + str(len(contours)))
        #cv2.drawContours(frame, contours, -1, (0, 0, 254), 3)
        cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()