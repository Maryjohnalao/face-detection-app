#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:23:23 2023

@author: anualao
"""


import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier("../file_dep/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("../file_dep/eye.xml")
face_cascade_ = cv2.CascadeClassifier("../file_dep/face.xml")

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
cap = cv2.VideoCapture("filename.mp4")

# video
def detect_faces():
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display
    cv2.imshow("img", img)
    # # Stop if escape key is pressed
    # k = cv2.waitKey(30) & 0xff
    # if k==27:
    # 	break
    # # Release the VideoCapture object
    # cap.release()
    # cv2.destroyAllWindows()


# image
def detect_faces_image(image):
    img = np.array(image.convert("RGB"))
    # img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade_.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img


def detect_eyes(image):
    new_img = np.array(image.convert("RGB"))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return img


def cartonize_image(image):
    new_img = np.array(image.convert("RGB"))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Edges
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    # Color
    color = cv2.bilateralFilter(img, 9, 300, 300)
    # Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


# detect_faces()