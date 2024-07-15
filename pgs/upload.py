import streamlit as st
import io
from PIL import Image

available_extenstions = ['png', 'jpg', 'jpeg']

def load_image():
    uploaded_file = st.file_uploader(
        label="Choose image",
        type=available_extenstions)
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


"""
# Upload
"""

img = load_image()
