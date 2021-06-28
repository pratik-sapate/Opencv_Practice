import cv2

video = cv2.VideoCapture('video/production.mp4')
fmog = cv2.createBackgroundSubtractorMOG2()

while video.isOpened():
    _, frame = video.read()
    if frame is None:
        break

    fgmask = fmog.apply(frame)
    blur = cv2.GaussianBlur(fgmask, (7, 7), 0)
    _, threshold = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(threshold, None, iterations=5)
    conture, his = cv2.findContours(fgmask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for con in conture:
        x, y, w, h = cv2.boundingRect(con)
        if w > 30 and h > 30:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
