import cv2
import numpy as np


cv2.namedWindow('tracking')

while True:
    image = cv2.imread('/home/pratik/Downloads/css-colors.jpg')
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(image_hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('image', mask)
    cv2.imshow('image_hsv', image_hsv)
    cv2.imshow('result', result)
    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
