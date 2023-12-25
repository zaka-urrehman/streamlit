import streamlit as st

# Create an empty container
container = st.empty()

# Check a condition
if st.checkbox("Show Content"):
    # Populate the container with content
    container.text("This content is dynamically added based on a condition.")
else:
    # Clear the container if the condition is not met
    container.empty()


# import streamlit as st
# import time

# with st.empty():
#     for seconds in range(10):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 10 seconds over!")

# st.write("Pakistan zinda bad")
