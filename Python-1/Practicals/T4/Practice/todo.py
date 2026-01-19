import streamlit as st

st.set_page_config(
    page_icon="📝",
    page_title="TODO",
    layout="centered"
)

st.title("Todo App")
st.header("Add Tasks")

# ✅ Initialize tasks list once
if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2 = st.columns(2)

with col1:
    task = st.text_input("Enter your task")

with col2:
    addcta = st.button("Add task")

# ✅ Add task
if addcta and task:
    st.session_state.tasks.append(task)
    st.success("Task added!")
    st.rerun()   # refresh UI cleanly

st.divider()

st.header("Your Tasks")

# ✅ Display tasks with checkboxes
for i, t in enumerate(st.session_state.tasks):
    completed = st.checkbox(t, key=f"task_{i}")

    if completed:
        st.success(f"Task '{t}' completed")
        st.session_state.tasks.pop(i)
