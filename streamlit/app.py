import streamlit as st
import time
from datetime import datetime
from todoproject.task import Task, TaskList, CriticalTask

def show_task_list(col):
    col.empty()
    if len(task_list.tasks) == 0:
        col.write("There are no tasks for now")
    else:
        for task in task_list.tasks:
            col.write(task.task_id) 
    return None


task_list = TaskList()

st.title("BGD-IA ToDo App")
col1, col2 = st.columns([0.3, 0.7])
menu = ["Add", "Remove", "Update"]
choice = col1.selectbox("Menu", menu)

show_task_list(col2)

if choice == "Add":
    col1.subheader("Add a new task")
    critical = col1.checkbox('Critical', key='critical')
    with col1.form('add-task'):
        name = st.text_input('Name',key='name')
        description = st.text_input('Description',key='description')
        deadline = None
        if critical:
            deadline = st.date_input('Deadline', min_value=datetime.now(), format="YYYY-MM-DD", key='deadline')
        if st.form_submit_button():
            task_list.add_task(name, description, critical, deadline)
            show_task_list(col2)
            # st.form.session_state.name = ""
            # st.form.session_state.description = ""
            # st.form.session_state.critical = False
            # st.form.session_state.deadline = datetime.now()


elif choice == "Remove":
    st.sidebar.subheader("Remove the existing")
   
elif choice == "Update":
    st.sidebar.subheader("Update the existing task")

