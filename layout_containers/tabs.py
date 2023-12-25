import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# Tab 1 - Cat
with tab1:
    st.header("Meow! It's a cat.")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    st.write("Here's some information about cats.")

# Tab 2 - Dog
with tab2:
    st.header("Woof! It's a dog.")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.write("Here's some information about dogs.")

# Tab 3 - Owl
with tab3:
    st.header("Hoot! It's an owl.")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    st.write("Here's some information about owls.")
    
    # Add an expander within the Owl tab
    with st.expander("Additional Owl Info"):
        st.write("This content is hidden by default in the Owl tab expander.")
        st.checkbox("Show hidden content")
