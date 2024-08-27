import cv2
import streamlit as st

def compress_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()

st.title("Video Compression App")
input_file = st.file_uploader("Upload your video file", type=["mp4", "mov","avi"])

if input_file is not None:
    output_file = f"compressed_{input_file.name}"
    compress_video(input_file.name, output_file)
    st.success(f"Compressed video saved as {output_file}")
