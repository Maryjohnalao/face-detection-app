#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:16:23 2023

@author: anualao
"""


import streamlit as st
import cv2
from PIL import Image, ImageEnhance
from app import detect_faces_image, detect_eyes, cartonize_image, face_cascade, cap

# function to apply detection to uploaded image
def apply_task_to_image(image_file):
    try:
        if image_file is not None:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded MRI.", use_column_width=True)

        # Face Detection
        task = ["Faces", "Eyes", "Cartonize"]
        feature_choice = st.sidebar.selectbox("Find Features", task)

        button = st.button("Process")
        if button:
            if feature_choice == "Faces":
                result_img = detect_faces_image(image)
                st.image(result_img)
            elif feature_choice == "Eyes":
                result_img = detect_eyes(image)
                st.image(result_img)
            else:
                result_img = cartonize_image(image)
                st.image(result_img, caption="Cartonized image", use_column_width=True)
    except:
        st.write("Upload an image to detect")


# function to apply detection to uploaded video
def apply_to_video(video_file):
    if video_file is not None:
        st.video(video_file)


# function to apply detection to image taken through camera
def apply_to_image_cam(image_file):
    try:
        if image_file is not None:
            image = Image.open(image_file)

        # Face Detection
        task = ["Faces", "Eyes", "Cartonize"]
        feature_choice = st.sidebar.selectbox("Find Features", task)

        button = st.button("Process")
        if button:
            if feature_choice == "Faces":
                result_img = detect_faces_image(image)
                st.image(result_img)
            elif feature_choice == "Eyes":
                result_img = detect_eyes(image)
                st.image(result_img)
            else:
                result_img = cartonize_image(image)
                st.image(result_img, caption="Cartonized image", use_column_width=True)
    except:
        st.write("Take a picture and save it to detect")


def main():
    st.title("Face Detection App")

    ##Options
    options = ["Upload an image", "Upload a video", "take a picture"]
    options_choice = st.sidebar.selectbox("Select Option", options)

    if options_choice == "Upload an image":
        image_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        apply_task_to_image(image_file)

    elif options_choice == "Upload a video":
        video_file = st.file_uploader("Upload a Video", type="mp4")
    else:
        img_file = st.camera_input("Take a picture")
        apply_to_image_cam(img_file)


if __name__ == "__main__":
    main()