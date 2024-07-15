import streamlit as st
from streamlit_webrtc import webrtc_streamer

mediaOptions = {
    "video": True,
    "audio": False
}

webrtc_streamer(key="sample", media_stream_constraints=mediaOptions)
