import datetime
import streamlit as st
import time

st.title("Pomodoro Timer")

col1, col2 = st.columns(2)
with col1:
    work_min = st.number_input(
        "Work duration (minutes)", min_value=1, max_value=60, value=25
    )
    subject = st.text_input(
        "Subject"
    )
with col2:
    break_min = st.number_input(
        "Break duration (minutes)", min_value=1, max_value=30, value=5
    )
st.markdown("---")

timer_placeholder = st.empty()
progress_bar = st.progress(0.0)

col_start, col_break = st.columns(2)
start_work = col_start.button(
    "Start work session", use_container_width=True
)
start_break = col_break.button("Start Break", use_container_width=True)


def run_timer(minutes, label, is_work=True):
    total_sec = minutes * 60
    for remaining in range(total_sec, -1, -1):
        mins, secs = divmod(remaining, 60)
        time_format = f"{mins:02d}:{secs:02d}"

        timer_placeholder.markdown(
             f"<h1 style='text-align: center; font-size: 72px; color: #FF4B4B;'>{label}: {time_format}</h1>",
            unsafe_allow_html=True,
        )

        progress = (total_sec - remaining) / total_sec
        progress_bar.progress(progress)
        time.sleep(1)

    if is_work:
        st.balloons()
        st.success(f"Session complete! Take a {break_min}-minute break.")

        if subject:
            hours_added = round(minutes / 60, 2)
            st.info(
                f"Saved {hours_added} hours under '{subject}'!"
            )
    else:
        st.snow()
        st.success("Break is over! Time to focus again.")

if start_work:
    run_timer(work_min, "Focus Time", is_work=True)
elif start_break:
    run_timer(break_min, "Rest", is_work=False)