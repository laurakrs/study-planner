import pandas as pd
import streamlit as st

st.title("Study Planner")
st.write(
    "Let's go!"
)


st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Pomodoro Timer", "Task Tracker", "Study Log", "Analytics"],
)

