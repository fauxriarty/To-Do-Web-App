import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo']=""


st.title("My To-Do List")
st.subheader("This app is to increase your productivity.")
st.write("Double click on the checkbox to finish the task.")

for index, todo in enumerate(todos): # gives us both index and its todo so that we can access the index of todo to be removed
    checkbox = st.checkbox(todo, key=todo)
    # key is the var todo so that each item in the checklist has its own unique key
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
    # 'if checkbox' since the checkbox= True when its clicked and when its not checked its False
    # so whenever user checks a checkbox then it becomes true hence that todo will be popped
    # del st.session_state[todo]
    # st._rerun()

st.text_input(label="Enter a to-do", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
