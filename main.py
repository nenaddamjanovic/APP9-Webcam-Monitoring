import time
from emailing import send_email
from cleaning import clean_folder
import glob
import os
import cv2
# install over terminal pip install opencv-python
# cv2 also includes nympy library

# Initialize video capture from the default camera
video = cv2.VideoCapture(0)
time.sleep(1)  # Wait for the camera to warm up

first_frame = None
status_list = []  # List to track motion status
count = 1

while True:
    status = 0  # No motion detected by default
    check, frame = video.read()  # Read a frame from the camera

    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau  # Set the first frame for comparison

    # Compute the absolute difference between the first frame and the current frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # Apply a binary threshold to the delta frame
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    # Dilate the threshold image to fill in holes
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Display the processed frame
    cv2.imshow("My video", dil_frame)

    # Find contours in the dilated frame
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:  # Ignore small contours
            continue
        x, y, w, h, = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        if rectangle.any():
            status = 1  # Motion detected

            cv2.imwrite(f"images/screenshot{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)  # Update the status list
    status_list = status_list[-2:]  # Keep only the last two status values

    # Check for motion (transition from detected to not detected)
    if status_list[0] == 1 and status_list[1] == 0:
        send_email(image_with_object)  # Send an email notification
        clean_folder()  # Clear folder of images

    # Display the original frame with rectangles
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
