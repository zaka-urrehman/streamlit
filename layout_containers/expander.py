import streamlit as st

# Create an expander with a label
with st.expander("Click to Expand"):
    st.write("This content is hidden by default and can be expanded by clicking.")

# Additional content outside the expander
st.write("This content is always visible.")
