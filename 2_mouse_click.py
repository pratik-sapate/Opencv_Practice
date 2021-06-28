import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
x1, y1, x2, y2 = 0, 0, 0, 0

def click_event(event, x, y, flags, param):
    global x1
    global y1
    global x2
    global y2
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        cv2.putText(image, str(x1)+','+str(y1), (x1, y1), 1, 1, (255, 255, 255), 1)
        cv2.imshow('ess', image)
    elif event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        cv2.putText(image, str(x2) + ',' + str(y2), (x2, y2), 1, 1, (255, 255, 255), 1)
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.imshow('ess', image)
    elif event == cv2.EVENT_:
        x2, y2 = x, y
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.imshow('ess', image)

image = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('ess', image)
cv2.setMouseCallback('ess', click_event)
cv2.waitKey(0)