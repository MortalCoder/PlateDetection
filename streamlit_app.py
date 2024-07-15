import streamlit as st

pg = st.navigation([
    st.Page("pgs/home.py", title="Home"),
    st.Page("pgs/upload.py", title="Upload"),
    st.Page("pgs/camera.py", title="Camera")
])

pg.run()
