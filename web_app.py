import streamlit as st
import function
import function


todo_list = function.read_todos_list()

def add_todo():
    new_todo_to_add = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo_to_add)
    function.write_todos_list(todo_list)


st.title("The Todo App")
st.subheader("This is a todo app")
st.write("This app will help you be more productive")

for index, todo in enumerate(todo_list):
    checkbox_list = st.checkbox(todo, key=todo)
    if checkbox_list:
        todo_list.pop(index)
        function.write_todos_list(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a new todo...",
              on_change=add_todo, key="new_todo")
