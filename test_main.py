import cv2
import streamlit as st
from datetime import datetime

st.title("Motion detector")
start = st.button("Start Camera")

if start:
    # If the "Start Camera" button is pressed, it initiates the camera.
    # Display Placeholder:
    # streamlit_image: Placeholder for displaying video frames.
    # Camera Initialization:
    # cv2.VideoCapture(0): Opens the default camera (0).
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
    # Converts the frame from BGR (OpenCV default) to RGB (for Streamlit).
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get current time
        now = datetime.now()

    # Adds the current day of the week to the frame at position (30, 80)
        cv2.putText(img=frame, text=now.strftime("$A"), org=(30,80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
    # Adds the current time (hour, minute, second) to the frame at position (30, 140)
        cv2.putText(img=frame, text=now.strftime("$H:%M:%S"), org=(30,140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
    # Updates the image in the Streamlit app with the annotated frame.
        streamlit_image.image(frame)