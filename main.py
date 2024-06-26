import time
import cv2
# install over terminal pip install opencv-python
# cv2 also includes nympy library


video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    cv2.imshow("My video", delta_frame)



    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()


print(check)
print(frame)