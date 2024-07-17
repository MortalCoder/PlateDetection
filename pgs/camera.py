import streamlit as st
import cv2
import av
from streamlit_webrtc import webrtc_streamer

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
    return av.VideoFrame.from_ndarray(img, format="bgr24")


mediaOptions = {
    "video": True,
    "audio": False
}

webrtc_streamer(
    key="sample",
    media_stream_constraints=mediaOptions,
    video_frame_callback=video_frame_callback,
    async_processing=True)
