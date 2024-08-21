import numpy as ny
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([])
    upper_blue = np.array([])

    cv2.imshow('frame', hsv)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


cv2.cvtColor([[255, 0, ]], cv2.COLOR_BGR2HSV)