import streamlit as st
import pandas as pd

st.title("Our Awesome VR Dashboard ✨")

# --- Let's create some FAKE data ---
fake_data = pd.DataFrame({
    'Player': ['Ana', 'Ben', 'Chloe', 'David', 'Eva'],
    'Session_Time_Minutes': [15, 25, 12, 31, 22],
    'Stress_Level': [3, 5, 2, 8, 4],
    'Puzzles_Solved': [5, 7, 4, 9, 6]
})

# --- Let's ORGANIZE our dashboard ---
st.divider() # This draws a nice line to separate things

# Create two columns
col1, col2 = st.columns(2)

# In the first column (col1), let's put our big number
with col1:
    st.metric(label="Total Players 👩‍🚀", value=len(fake_data))
    
    # Let's add another metric!
    avg_session_time = fake_data['Session_Time_Minutes'].mean()
    st.metric(label="Avg. Session Time ⏰", value=f"{avg_session_time:.1f} min")

# In the second column (col2), let's put our chart
with col2:
    st.bar_chart(data=fake_data, x='Player', y='Stress_Level')
