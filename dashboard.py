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
# --- SIDEBAR ---
st.sidebar.image("logo.png", width=200) # Show your logo

st.sidebar.header("Analytics")

# This is how we make the "General User Insights" link look selected
st.sidebar.markdown("""
<a href="#" style="
    padding: 0.5rem 1rem;
    background-color: #E6F2FE;
    color: #1C64F2;
    border-radius: 0.5rem;
    text-decoration: none;
    font-weight: bold;
">General User Insights</a>
""", unsafe_allow_html=True)

# These are the other links, now with bigger text!
st.sidebar.markdown('<p style="font-size: 18px;">Calm</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Energy</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Awe</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Pain Relief</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Focus</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Sleep</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="font-size: 18px;">Manage</p>', unsafe_allow_html=True)

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

# --- USER INSIGHTS ---
st.subheader("User insights")

# Here are the numbers from your design
play_count = "2,200,000"
avg_time = "21.8 min"
enjoyability_rating = "500"
last_month_count = "1,500"

# Create invisible columns to center the content
_ , center_col, _ = st.columns([1, 2, 1]) # Left space, main content, right space

# Put everything inside the center column
with center_col:
    # Use a container with a border to group everything
    with st.container(border=True):
        # ROW 1
        row1_col1, row1_col2, row1_col3 = st.columns([1, 5, 2])
        with row1_col1:
            st.markdown("### 🎮")
        with row1_col2:
            st.markdown("#### Play count")
        with row1_col3:
            st.markdown(f"### {play_count}")

        st.divider()

        # ROW 2
        row2_col1, row2_col2, row2_col3 = st.columns([1, 5, 2])
        with row2_col1:
            st.markdown("### ⏳")
        with row2_col2:
            st.markdown("#### Average time using Liminal")
            st.markdown("_(From log in to log out)_")
        with row2_col3:
            st.markdown(f"### {avg_time}")
            
        st.divider()

        # ROW 3
        row3_col1, row3_col2, row3_col3 = st.columns([1, 5, 2])
        with row3_col1:
            st.markdown("### ⭐")
        with row3_col2:
            st.markdown("#### 4 & 5 Enjoyability Rating")
        with row3_col3:
            st.markdown(f"### {enjoyability_rating}")
            
        st.divider()

        # ROW 4
        row4_col1, row4_col2, row4_col3 = st.columns([1, 5, 2])
        with row4_col1:
            st.markdown("### 👓")
        with row4_col2:
            st.markdown("#### Last Month play count")
        with row4_col3:
            st.markdown(f"### {last_month_count}")
