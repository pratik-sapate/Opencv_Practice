import cv2
import numpy as np

def detect_red(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 130, 150), (255, 255, 255))
    imask = mask > 0
    red = np.zeros_like(image, np.uint8)
    red[imask] = image[imask]
    return red

def detect_green(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (60, 40, 25), (75, 255, 255))
    imask = mask > 0
    green = np.zeros_like(image, np.uint8)
    green[imask] = image[imask]
    return green
# if __name__ == '__main__':
#     image = cv2.imread("/home/pratik/Downloads/color_shade.jpg")
#     detect_green(image)
#     # detect_red(image)
#     cv2.imshow("original", image)
#     cv2.waitKey(0)

if __name__ == '__main__':
    video = cv2.VideoCapture(0)
    while video.isOpened():
        _, frame = video.read()
        red_image = detect_red(frame)
        cv2.imshow('my image', cv2.hconcat((frame, red_image)))
        if cv2.waitKey(1) & 0xff == ord("q"):
            break