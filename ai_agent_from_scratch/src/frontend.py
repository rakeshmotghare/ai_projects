import streamlit as st
import ai_projects.ai_agent_from_scratch.src.agent as agent

st.set_page_config(page_title="First AI Agent using python", page_icon=":robot_face:")
st.title("AI Agent")
st.caption("Weather, calculator, and currency conversion -- no framework, just Python.")

# st.session_state.messages is this app's memory -- it survives Streamlit's
# re-runs on every interaction, which a plain local variable would not.
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] in ("user", "assistant") and message.get("content"):
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_input = st.chat_input("Ask about the weather, do some maths, or convert a currency...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = agent.run_agent(st.session_state.messages)
        st.write(answer)