import pandas as pd
import streamlit as st
from google.cloud import firestore

st.title("Study Planner")
st.write(
    "Let's go!"
)


# Initialize tasks and logs in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "logs" not in st.session_state:
    st.session_state.logs = []

tasks_df = pd.DataFrame(st.session_state.tasks)
logs_df = pd.DataFrame(st.session_state.logs)

col1, col2, col3 = st.columns(3)

total_tasks = len(tasks_df) if not tasks_df.empty else 0
completed_tasks = (
    int(tasks_df["done"].sum())
    if not tasks_df.empty and "done" in tasks_df
    else 0
)

total_hours = 0.0
if len(st.session_state["logs"]) > 0:
    logs_df = pd.DataFrame(st.session_state["logs"])
    if "hours" in logs_df.columns:
        total_hours = float(
            pd.to_numeric(logs_df["hours"], errors="coerce").sum()
        )

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed Tasks", completed_tasks)
col3.metric("Total Hours Studied", f"{total_hours:.2f} hrs")

st.markdown("---")


st.subheader("Pending Tasks")

if not tasks_df.empty and "done" in tasks_df:
    pending = tasks_df[tasks_df["done"] == False]
    if not pending.empty:
        st.dataframe(
            pending[["subject", "task", "due_date"]],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.success("No pending tasks! Great job 🎉")
else:
    st.info(
        "No tasks added yet. Go to **Task Tracker** in the sidebar to add your first task."
    )

st.markdown("---")


st.subheader("Recent Study Sessions")

if not logs_df.empty:
    st.dataframe(
        logs_df.sort_values(by="log_date", ascending=False).head(5)[
            ["subject", "hours", "log_date"]
        ],
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info(
        "No study sessions logged yet. Use the **Pomodoro Timer** or **Study Log** to record study time."
    )

