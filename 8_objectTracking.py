import cv2


def check_overlapping_rectangle(conture):
    required_contures = []
    conture.sort(key=lambda x: cv2.contourArea(x))
    for index in range(len(conture)):
        x1, y1, w1, h1 = cv2.boundingRect(conture[index])
        flag = True
        for index2 in range(index+1, len(conture)):
            x2, y2, w2, h2 = cv2.boundingRect(conture[index2])
            contains = x1 >= x2 and y1 >= y2 and w1 <= w2 and h1 <= h2
            if contains:
                flag = False
        if flag:
            required_contures.append(conture[index])

    return required_contures


def tracking_moving_object(video_file):
    video = cv2.VideoCapture(video_file)
    _, frame1 = video.read()
    _, frame2 = video.read()
    while video.isOpened():
        original = frame1.copy()
        frame = cv2.absdiff(frame1, frame2)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(frame_gray, (7, 7), 0)
        _, threshold = cv2.threshold(blur, 30, 255, cv2.THRESH_BINARY)
        dilate = cv2.dilate(threshold, None, iterations=5)
        conture, his = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        conture = check_overlapping_rectangle(conture)
        for con in conture:
            x, y, w, h = cv2.boundingRect(con)
            cv2.rectangle(original, (x, y), (x+w, y+h), (0, 255, 0), 1)
        # cv2.drawContours(original, conture, -1, (0, 255, 0), -1)
        cv2.imshow('video', original)
        frame1 = frame2
        _, frame2 = video.read()
        if cv2.waitKey(1) & 0xff == ord("q"):
            break


if __name__ == '__main__':
    tracking_moving_object('video/production.mp4')
