import streamlit as st
from auth.authentication import login  # your login function

# Page configuration
st.set_page_config(page_title="Login Page", layout="centered")

# Authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()  # Render login page
    st.stop()
