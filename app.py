import streamlit as st
from auth.authentication import login  # your login function
from blue_horizon import main as dashboard  # Import the dashboard function

# Page configuration
st.set_page_config(page_title="Login Page", layout="centered")

# Check if the user is authenticated
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# If the user is authenticated, show the dashboard
if st.session_state["authenticated"]:
    dashboard()  # Render dashboard
else:
    # If not authenticated, show the login page
    login()  # Render login page
    st.stop()  # Stop the execution to prevent dashboard from loading when not authenticated
