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
      # --- AWE INTENSITY GAUGE ---
st.divider()

# We need to import plotly's graph objects for this chart
import plotly.graph_objects as go

# 1. Define the value for our gauge
awe_intensity = 70

# 2. Create the gauge chart figure
fig_gauge = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = awe_intensity,
    number = {'suffix': "%"}, # CHANGE 1: Added a suffix to show the '%' symbol
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Awe Intensity", 'font': {'size': 24}},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "#8A2BE2"}, # This bar now clearly represents the 70%
        # CHANGE 2: Removed the confusing 'steps' for a cleaner look
    }))

fig_gauge.update_layout(
    paper_bgcolor = "rgba(0,0,0,0)", # Makes the background transparent
    font = {'color': "white", 'family': "Arial"}
)

# 3. Display the chart in a centered column
_ , center_col, _ = st.columns([1, 2, 1])
with center_col:
    st.plotly_chart(fig_gauge, use_container_width=True)
 # --- CATEGORY PREFERENCES DONUT CHART ---
st.divider()

# 1. Prepare the data from your design
category_data = pd.DataFrame({
    'Category': ['Energy', 'Awe', 'Calm', 'Sleep', 'Focus', 'Pain Relief'],
    'Percentage': [34, 26, 18, 13, 5, 4]
})

# Define the colors for each category to match the design
category_colors = ['#f28e2b', '#AF7AC5', '#2E86C1', '#28B463', '#5DADE2', '#1E8449']

# 2. Create the donut chart figure
fig_donut = go.Figure(data=[go.Pie(
    labels=category_data['Category'],
    values=category_data['Percentage'],
    hole=.6,
    marker_colors=category_colors,
    textinfo='percent',
    textfont_size=16,
    textposition='outside',
    insidetextorientation='horizontal',
    hovertemplate="<b>%{label}</b><br>%{percent}<extra></extra>"
)])

# 3. Update the layout to match your design
fig_donut.update_layout(
    # CHANGE 1: The title is now fully handled by st.markdown below
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5,
        font=dict(size=16)
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    font = {'color': "white", 'family': "Arial"}
)

# 4. Display the chart in a centered section
_ , center_col, _ = st.columns([1, 4, 1])
with center_col:
    st.markdown("<h3 style='text-align: center;'>Category Preferences</h3>", unsafe_allow_html=True)
    # CHANGE 2: Added a centered markdown for the subtitle to ensure perfect alignment
    st.markdown("<p style='text-align: center;'>Where Users Spend the Most Time or User Engagement by Category</p>", unsafe_allow_html=True)
    st.plotly_chart(fig_donut, use_container_width=True)
# --- MOST EFFECTIVE EXPERIENCES TABLE (NEW NATIVE METHOD) ---
st.divider()

# 1. Prepare the data for the table
table_data = pd.DataFrame({
    "Category": ["Calm", "Energy", "Awe", "Focus", "Pain Relief", "Sleep"],
    "Top Experience": ["Aureole Hypnosis", "Cyber Punch", "Samsara", "Rhythmic Flow", "Aureole Relief", "Retreat"],
    "Effectiveness Score": ["4.8 ⭐", "4.7 ⭐", "4.5 ⭐", "4.1 ⭐", "4.4 ⭐", "4.5 ⭐"],
    "Image": [
        "https://i.imgur.com/7Z2WJ44.png",
        "https://i.imgur.com/KDKk3sT.png",
        "https://i.imgur.com/SztmG3z.png",
        "https://i.imgur.com/wPzL6aY.png",
        "https://i.imgur.com/7Z2WJ44.png",
        "https://i.imgur.com/A4y9j2N.png"
    ]
})

# 2. Display the section title in a centered column
_ , center_col, _ = st.columns([1, 10, 1])
with center_col:
    st.markdown("<h3 style='text-align: center;'>Most Effective Experiences Per Category</h3>", unsafe_allow_html=True)
    
    # 3. Create a header row using columns
    header_cols = st.columns([2, 3, 2, 2])
    header_cols[0].markdown("**Category**")
    header_cols[1].markdown("**Top Experience**")
    header_cols[2].markdown("**Effectiveness Score**")
    header_cols[3].markdown("**Image**")
    
    st.divider()

    # 4. Loop through the data and create a row for each experience using columns
    for index, row in table_data.iterrows():
        row_cols = st.columns([2, 3, 2, 2])
        row_cols[0].write(row['Category'])
        row_cols[1].write(row['Top Experience'])
        row_cols[2].write(row['Effectiveness Score'])
        row_cols[3].image(row['Image'], width=120)
        st.divider()
# --- USER PANEL IN SIDEBAR ---
# Add this at the end of all your st.sidebar calls
st.sidebar.divider()

user_panel_html = """
<div style="font-family: Arial; font-size: 18px;">
    <p style="font-weight: bold;">SwinUniversity</p>
    <p>PaolaAdmin ➡️</p>
</div>
"""
st.sidebar.markdown(user_panel_html, unsafe_allow_html=True)
st.sidebar.button("Manage")
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