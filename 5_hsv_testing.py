import cv2
import numpy as np

b, g, r = 0, 0, 0


def do(x):
    b = x

image = cv2.imread('/home/pratik/Downloads/css-colors.jpg')
w, h, c = image.shape
image2 = np.zeros((w, h, c), np.uint8)
cv2.imshow('image', image)

cv2.createTrackbar('Blue', 'image', 0, 255, do)
cv2.createTrackbar('Green', 'image', 0, 255, do)
cv2.createTrackbar('Red', 'image', 0, 255, do)
while True:
    image = cv2.imread('/home/pratik/Downloads/css-colors.jpg')
    b = cv2.getTrackbarPos('Blue', 'image')
    g = cv2.getTrackbarPos('Green', 'image')
    r = cv2.getTrackbarPos('Red', 'image')
    image2[:] = [b, g, r]
    image = cv2.bitwise_xor(image, image2)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
