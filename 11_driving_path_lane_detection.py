import cv2
import numpy as np

video = cv2.VideoCapture('video/driving.mp4')

while video.isOpened():
    ret, frame = video.read()
    mask = np.zeros_like(frame)
    mask_color = (255,) * frame.shape[2]
    h, w, _ = frame.shape
    roi = [(0, h), (0, h - h / 4), (w / 2, h / 2), (w, h - h / 4), (w, h)]
    cv2.fillPoly(mask, np.array([roi], np.int32), mask_color)

    frame_canny = cv2.Canny(frame, 0, 200, apertureSize=3)
    hough_line = cv2.HoughLinesP(frame_canny, 1, np.pi / 180, 160, minLineLength=40, maxLineGap=25, lines=np.array([]))

    for line in hough_line:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
    frame = cv2.bitwise_and(frame, mask)
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
