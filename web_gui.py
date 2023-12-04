import streamlit as st
import functions

todos = functions.get_todo()

st.title("My To-Do App")
st.subheader("This is my to-do app")
st.text("This app is used to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...."
                                    "")

