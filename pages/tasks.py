import datetime
import streamlit as st

st.title("Tasks")

# Ensure session state tasks container exists
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Form to create new task
with st.expander("Add New Task"):
    with st.form("new_task_form"):
        subject = st.text_input("Subject")
        task_desc = st.text_input("Task Description")
        due_date = st.date_input("Due Date", datetime.date.today())
        submitted = st.form_submit_button("Add Task")

        if submitted and subject and task_desc:
            new_id = len(st.session_state.tasks) + 1
            st.session_state.tasks.append(
                {
                    "id": new_id,
                    "subject": subject,
                    "task": task_desc,
                    "due_date": str(due_date),
                    "done": False,
                }
            )
            st.success("Task added!")
            st.rerun()

st.subheader("Task List")

if st.session_state.tasks:
    for idx, item in enumerate(st.session_state.tasks):
        c1, c2, c3, c4 = st.columns([1, 3, 2, 1])

        is_done = c1.checkbox("", value=item["done"], key=f"task_check_{idx}")
        if is_done != item["done"]:
            st.session_state.tasks[idx]["done"] = is_done
            st.rerun()

        c2.write(f"**{item['subject']}**: {item['task']}")
        c3.write(f"Due: {item['due_date']}")

        if c4.button("delete", key=f"task_del_{idx}"):
            st.session_state.tasks.pop(idx)
            st.rerun()
else:
    st.info("No tasks added yet.")