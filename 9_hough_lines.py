import cv2
import numpy as np

image = cv2.imread('images/sudoku.jpg')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_canny = cv2.Canny(image_grey, 50, 150, apertureSize=3)
haugh_lines = cv2.HoughLines(image_canny, 1, np.pi/180, 250)

for line in haugh_lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    # c = x.cos@ + y.sin@
    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 2000 * (-b))
    y1 = int(y0 + 2000 * a)
    # cv2.circle(image, (x1, y1), 4, (0, 255, 0), -1)
    x2 = int(x0 - 2000 * (-b))
    y2 = int(y0 - 2000 * a)

    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

cv2.imshow('image_canny', image_canny)
cv2.imshow('image', image)
cv2.waitKey(0)