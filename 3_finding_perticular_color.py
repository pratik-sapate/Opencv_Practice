import cv2
import numpy as np

def nochange(x):
    pass
    # print(x)

cv2.namedWindow('image')
cv2.createTrackbar('lower_H', 'image', 0, 255, nochange)
cv2.createTrackbar('lower_S', 'image', 0, 255, nochange)
cv2.createTrackbar('lower_V', 'image', 0, 255, nochange)

cv2.createTrackbar('higher_H', 'image', 0, 255, nochange)
cv2.createTrackbar('higher_S', 'image', 0, 255, nochange)
cv2.createTrackbar('higher_V', 'image', 0, 255, nochange)


while True:
    image = cv2.imread('/home/pratik/Downloads/css-colors.jpg')
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos('lower_H', 'image')
    ls = cv2.getTrackbarPos('lower_S', 'image')
    lv = cv2.getTrackbarPos('lower_V', 'image')
    hh = cv2.getTrackbarPos('higher_H', 'image')
    hs = cv2.getTrackbarPos('higher_S', 'image')
    hv = cv2.getTrackbarPos('higher_V', 'image')
    lower = np.array([lh, ls, lv])
    higher = np.array([hh, hs, hv])
    mask = cv2.inRange(img_hsv, lower, higher)
    res = cv2.bitwise_and(image, image, mask=mask)
    image = cv2.hconcat([image, res])
    cv2.imshow('image', res)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
