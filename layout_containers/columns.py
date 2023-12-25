import streamlit as st



col1, col2, col3 = st.columns(3)



with col1:
   st.header("This is col 1")

with col2:
   st.header("This is col 2")

with col3:
   st.header("This is col 3")
