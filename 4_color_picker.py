import cv2
import numpy as np


def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        blue = image[y, x, 0]
        green = image[y, x, 1]
        red = image[y, x, 2]
        my_image = np.zeros((512, 512, 3), np.uint8)
        my_image[:] = [blue, green, red]
        cv2.imshow('image', image)
        cv2.imshow('color_picker', my_image)


image = cv2.imread('/home/pratik/Downloads/css-colors.jpg')
cv2.imshow('image', image)
cv2.setMouseCallback('image', on_mouse_click)
cv2.waitKey(0)
