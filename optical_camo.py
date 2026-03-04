import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0
for i in range(30):
    ret, background = cap.read()

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret: break
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    res2 = cv2.bitwise_and(bg_image, bg_image, mask=mask)
    
    cv2.imshow("Optical Camo", res2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()