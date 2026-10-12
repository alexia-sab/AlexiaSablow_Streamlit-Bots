import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# with st.chat_message("user"):
#   st.write("Hello!")

# prompt = st.chat_input("Say something! ")
# if prompt:
#   st.write(f"User has sent the following prompt: {prompt}")
