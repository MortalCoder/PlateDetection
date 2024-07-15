import streamlit as st

css='''
<style>
    section.main > div {max-width:100rem}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

st.camera_input("Bruh")
