import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- PAGE CONFIG ---
# This is a magic Streamlit command that needs to be the first thing in your app
st.set_page_config(
    page_title="Liminal VR Analytics",
    page_icon="🧠", # This is the icon that shows up in the browser tab
    layout="wide" # This makes the page use the full width
)
# --- CUSTOM SIDEBAR ---

# 1. Hide the default Streamlit navigation
st.markdown("""<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>""", unsafe_allow_html=True)

# 2. Logo at the top
st.sidebar.image("logo.png", width=200)

# 3. "Analytics" header
st.sidebar.header("Analytics")

# 4. Custom navigation links
# This section now includes links for all your pages.
st.sidebar.page_link("Dashboard.py", label="General User Insights", icon="📊")
st.sidebar.page_link("pages/2_Calm.py", label="Calm")
st.sidebar.page_link("pages/3_Energy.py", label="Energy")
st.sidebar.page_link("pages/4_Awe.py", label="Awe")
st.sidebar.page_link("pages/5_Pain_Relief.py", label="Pain Relief")
st.sidebar.page_link("pages/6_Focus.py", label="Focus")
st.sidebar.page_link("pages/7_Sleep.py", label="Sleep")

# 5. User Panel at the bottom
st.sidebar.divider()
user_panel_html = """
<div style="font-family: Arial; font-size: 18px;">
    <p style="font-weight: bold;">SwinUniversity</p>
    <p>PaolaAdmin ➡️</p>
</div>
"""
st.sidebar.markdown(user_panel_html, unsafe_allow_html=True)
st.sidebar.button("Manage")
# --- MAIN CONTENT ---
st.title("Analytics Dashboard")
st.markdown("This dashboard provides key insights into how Liminal's VR experiences influence well-being and engagement.")

st.divider() # This draws a line

# --- FILTERS ---
st.subheader("Filters")

# Create four columns for the filters
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.selectbox("Username", options=["All", "Ana", "Ben", "Chloe"])

with col2:
    st.selectbox("Organization", options=["All", "Company A", "Company B"])
    
with col3:
    st.selectbox("Device ID", options=["All", "Device 1", "Device 2"])

with col4:
    # Set default dates for the date picker
    today = datetime.now()
    start_date = today - timedelta(days=48)
    
    st.date_input(
        "Select date range",
        (start_date, today), # Use today as the end date
        format="YYYY/MM/DD"
    )

# Put the button below the filters
st.button("Export Report PDF", use_container_width=True)
# --- FOOTER ---
st.divider()

# Using markdown with HTML/CSS for a custom footer
# NOTE: Replace '#' in the links and the image URLs with your actual links and images.
footer_html = """
<style>
    .footer { text-align: center; padding: 2rem 0; color: #A9A9A9; }
    .footer .logo-img { width: 120px; margin-bottom: 1rem; }
    .footer .social-icons img { width: 24px; margin: 0 10px; }
    .footer .footer-links a { color: #A9A9A9; text-decoration: none; margin: 0 10px; }
</style>
<div class="footer">
    <img src="logo.png" class="logo-img">
    <p>© 2025 - Liminal VR</p>
    <div class="social-icons">
        <a href="#"><img src="https://i.imgur.com/4z15M62.png"></a>
        <a href="#"><img src="https://i.imgur.com/1Gj2Z2F.png"></a>
        <a href="#"><img src="https://i.imgur.com/4z15M62.png"></a>
        <a href="#"><img src="https://i.imgur.com/1Gj2Z2F.png"></a>
        <a href="#"><img src="https://i.imgur.com/4z15M62.png"></a>
    </div>
    <div class="footer-links">
        <a href="#">ABOUT US</a> - 
        <a href="#">CONTACT</a> - 
        <a href="#">TERMS OF SERVICE</a> - 
        <a href="#">PRIVACY POLICY</a>
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

