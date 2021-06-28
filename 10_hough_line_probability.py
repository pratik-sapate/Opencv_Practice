import cv2
import numpy as np


image = cv2.imread('images/road_EPS213.jpg')
h, w, _ = image.shape
roi = [(0, h), (0, h-h/4), (w/2, h/2), (w, h-h/4), (w, h)]

# image_canny = cv2.GaussianBlur(image_canny, (3, 3), 100)

mask = np.zeros_like(image)
mask_color = (255, ) * image.shape[2]

cv2.fillPoly(mask, np.array([roi], np.int32), mask_color)
image = cv2.bitwise_and(image, mask)
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_canny = cv2.Canny(image, 0, 255, apertureSize=3)
hough_line = cv2.HoughLinesP(image_canny, 1, np.pi/180, 160, minLineLength=40, maxLineGap=25, lines=np.array([]))
cv2.imshow('image2', image_canny)

for line in hough_line:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

cv2.imshow('image', image)
cv2.waitKey(0)