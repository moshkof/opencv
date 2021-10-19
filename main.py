import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:P123456i@192.168.18.112/sub')
# cap.set(3, 500)
# cap.set(4, 400)

while True:
    success, img = cap.read()
    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


# cv2.waitKey(0)





# img = cv2.imshow('result', img)

# mat = np.zeros(, dtype='float32')

# cv2.imshow(img, mat, dtype='uint8')

