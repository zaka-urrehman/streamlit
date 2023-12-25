import streamlit as st

# Render something outside the container
st.title("Outside Container")

# Open a container using "with" and render something inside the container
with st.container():
    st.title("Inside Container")
    st.write("This is some content inside the container.")
    st.write("You can add more content here.")

# Render something outside the container again
st.title("Back Outside Container")
st.write("This is outside the container.")

