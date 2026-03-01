import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config
st.set_page_config(
    page_title="Traffic Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read the HTML file
html_file_path = "traffic_dashboard.html"

# Custom CSS to force the iframe to take full height
st.markdown("""
    <style>
        .block-container {
            padding: 0rem !important;
            max-width: 100%;
        }
        .stApp {
            margin: 0;
            padding: 0;
        }
        iframe {
            height: 100vh !important;
            width: 100vw !important;
            border: none;
            margin: 0;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Nhúng API_KEY từ mảng Secrets của bảng điều khiển Streamlit
    api_key = "sk-fake-key-for-local-demo" # Giá trị mặc định (phòng khi không có secrets)
    try:
        if "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass # Nếu chạy local không cấu hình .streamlit/secrets.toml
        
    html_content = html_content.replace('TO_BE_REPLACED_BY_BACKEND', api_key)
    
    # Use components.html to render the dashboard
    components.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error(f"Error: Could not find {html_file_path}. Please ensure it is in the same directory as this script.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
