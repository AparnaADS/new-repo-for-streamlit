import streamlit as st
import json
from config.constants import USERS_DATA_PATH
from PIL import Image

def authenticate_user(email, password):
    """Authenticate user against users.json"""
    try:
        with open(USERS_DATA_PATH, "r") as f:
            users_data = json.load(f)
        user = next((u for u in users_data["users"]
                     if u["username"] == email and u["password"] == password), None)
        return user
    except Exception:
        return None

def login():
    """Render Blue Horizon styled login page"""
    st.set_page_config(page_title="Blue Horizon Login", layout="centered")

    # --- CSS Styling ---
    st.markdown("""
        <style>
        div[data-testid="stDecoration"],
        div[data-testid="stHeader"],
        div[data-testid="stToolbar"],
        .stApp > header {
            display: none !important;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77, #778da9);
            color: #333;
        }

        .login-container {
            background: white;
            padding: 40px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            width: 420px;
            margin: 8% auto;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }

        .login-container h2 {
            color: #1b263b;
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }

        .separator {
            height: 6px;
            background: linear-gradient(to right, #f5c518, #f7d774, #f5c518);
            border-radius: 3px;
            width: 100%;
            margin: 18px 0;
        }

        .subtitle {
            color: #1b263b !important; /* Added !important to ensure override */
            font-size: 18px !important; /* Added !important to ensure override */
            font-weight: 600;
            text-align: center;
            line-height: 1.6;
        }

        .stTextInput>div>div>input {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-size: 14px;
        }

        .stButton>button {
            width: 100%;
            padding: 13px;
            background: linear-gradient(135deg, #1b263b, #415a77);
            border: none;
            border-radius: 10px;
            color: white !important;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #0d1b2a, #1b263b);
        }
        
        /* New CSS to target the container directly */
        div[data-testid="stVerticalBlock"] > div:first-of-type > .element-container {
            background-color: white;
            padding: 40px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            width: 420px;
            margin: 8% auto;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Login Card using Streamlit components ---
    with st.container():
        st.markdown('<div class="login-container-wrapper">', unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align:center;">
                <h2>
                    <span style="font-family:'Apple Color Emoji','Segoe UI Emoji','NotoColorEmoji',sans-serif;color:unset;">🔒</span>
                    Blue Horizon Login
                </h2>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
        
        # Updated subtitle, separated into two lines for styling
        st.markdown('<p class="subtitle">Welcome to Blue Horizon International Analytics Dashboard</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle" style="margin-top:10px;">Please enter your credentials to continue</p>', unsafe_allow_html=True)
        
        # Inputs + button directly
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        if st.button("Login"):
            user = authenticate_user(email, password)
            if user:
                st.success(f"✅ Welcome, {user['username']}!")
                st.session_state["authenticated"] = True
                st.session_state["user_companies"] = user["companies"]
            else:
                st.error("❌ Invalid email or password. Please try again.")
        
        st.markdown('</div>', unsafe_allow_html=True)