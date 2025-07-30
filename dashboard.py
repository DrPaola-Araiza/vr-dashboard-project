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
# --- EMOTION AND MENTAL STATES SHIFTS ---
st.divider()

# We need these new libraries
import plotly.express as px
import circlify # Our new tool for packing circles

# Create invisible columns to center this whole section
_ , center_col, _ = st.columns([1, 4, 1])

with center_col:
    # Centered title and description
    st.markdown("<h2 style='text-align: center;'>Emotion and mental states shifts</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>The bubbles below show users' overall emotional states before and after using the Liminal Platform.</p>", unsafe_allow_html=True)

    # Prepare the data for the bubbles
    before_data = pd.DataFrame({
        'mood': ["Anxious", "Irritated", "Pain", "Bored", "Sad", "Excited", "Relax", "Cheerful", "Calm", "Focus", "Rested", "Mental vitality"],
        'size': [30, 25, 28, 22, 20, 10, 18, 9, 15, 8, 9, 7],
    })

    after_data = pd.DataFrame({
        'mood': ["Calm", "Excited", "Relax", "Focus", "Cheerful", "Rested", "Mental vitality", "Anxious", "Irritated", "Pain", "Bored", "Sad"],
        'size': [30, 28, 29, 25, 26, 24, 22, 8, 7, 9, 6, 5],
    })

    # Calculate bubble positions using circlify
    before_circles = circlify.circlify(before_data['size'].tolist(), show_enclosure=False)
    after_circles = circlify.circlify(after_data['size'].tolist(), show_enclosure=False)

    before_data['x'] = [c.x for c in before_circles]
    before_data['y'] = [c.y for c in before_circles]
    after_data['x'] = [c.x for c in after_circles]
    after_data['y'] = [c.y for c in after_circles]

    # Define the specific color for each mood
    mood_color_map = {
        "Calm": "#2ca02c", "Excited": "#98df8a", "Relax": "#55a630", "Cheerful": "#80b918", "Rested": "#aacc00",
        "Anxious": "#d62728", "Irritated": "#ff6b6b", "Bored": "#c44536", "Pain": "#8d0801",
        "Sad": "#1f77b4",
        "Focus": "#ffc300", "Mental vitality": "#ffd60a"
    }

    # Create three columns for the charts and the divider line
    col1, mid_col, col2 = st.columns([10, 1, 10])

    with col1:
        st.subheader("Before")
        fig_before = px.scatter(
            before_data, x='x', y='y', size='size', color='mood', text='mood',
            color_discrete_map=mood_color_map,
            size_max=60
        )
        fig_before.update_traces(textposition='middle center', textfont=dict(color='white', size=14))
        # This part cleans up the chart to look like your design
        fig_before.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(visible=False),
            # CHANGE: Added 'scaleanchor' and 'scaleratio' to make the chart a square
            yaxis=dict(visible=False, scaleanchor="x", scaleratio=1)
        )
        st.plotly_chart(fig_before, use_container_width=True)

    with mid_col:
        st.markdown("<div style='width: 2px; height: 400px; background-color: #333; margin: auto;'></div>", unsafe_allow_html=True)

    with col2:
        st.subheader("After")
        fig_after = px.scatter(
            after_data, x='x', y='y', size='size', color='mood', text='mood',
            color_discrete_map=mood_color_map,
            size_max=60
        )
        fig_after.update_traces(textposition='middle center', textfont=dict(color='white', size=14))
        # This part cleans up the chart to look like your design
        fig_after.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(visible=False),
            # CHANGE: Added 'scaleanchor' and 'scaleratio' to make the chart a square
            yaxis=dict(visible=False, scaleanchor="x", scaleratio=1)
        )
        st.plotly_chart(fig_after, use_container_width=True)

    st.divider()

    # New centered table for the summary stats
    summary_col1, summary_col2 = st.columns(2)
    with summary_col1:
        st.markdown("""
        <p style="font-size: 20px; text-align: right;">
            <span style="color: #2ca02c;">▲</span> Positive Moods Increased by
        </p>
        """, unsafe_allow_html=True)
    with summary_col2:
        st.markdown("""
        <p style="font-size: 20px; text-align: left; font-weight: bold;">
            53.9%
        </p>
        """, unsafe_allow_html=True)

    summary_col3, summary_col4 = st.columns(2)
    with summary_col3:
        st.markdown("""
        <p style="font-size: 20px; text-align: right;">
            <span style="color: #d62728;">▼</span> Negative Moods Decrease by
        </p>
        """, unsafe_allow_html=True)
    with summary_col4:
        st.markdown("""
        <p style="font-size: 20px; text-align: left; font-weight: bold;">
            20.8%
        </p>
        """, unsafe_allow_html=True)