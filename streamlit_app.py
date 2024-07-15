import streamlit as st


pg = st.navigation([
    st.Page("home.py", title="Home"),
    st.Page("ml/camera.py", title="Camera"),
    st.Page("ml/upload.py", title="Upload")
])

st.set_page_config(layout="wide")

pg.run()
