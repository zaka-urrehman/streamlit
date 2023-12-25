import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)



# Add an expander in the sidebar
with st.sidebar.expander("Additional Options"):
    # Content inside the expander
    st.write("This content is hidden by default in the sidebar expander.")
    st.checkbox("Show hidden content")

# Additional content outside the sidebar
st.write("This content is outside the sidebar.")
