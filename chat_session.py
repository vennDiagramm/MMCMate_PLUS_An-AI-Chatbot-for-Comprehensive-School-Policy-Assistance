import streamlit as st

def init_chat():
    """Initialize in-memory chat session"""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role, content):
    """Add a message to the current session"""
    st.session_state.messages.append({"role": role, "content": content})

def display_chat():
    """Display current chat messages"""
    for message in st.session_state.messages:
        avatar = (
            'https://raw.githubusercontent.com/vennDiagramm/MMCMate_An_AI_Chatbot_for_School_Policy_Assistance/main/icons/user_icon.ico'
            if message["role"] == "user"
            else 'https://raw.githubusercontent.com/vennDiagramm/MMCMate_An_AI_Chatbot_for_School_Policy_Assistance/main/icons/mapua_icon_83e_icon.ico'
        )
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(f"<div style='text-align: justify;'>{message['content']}</div>", unsafe_allow_html=True)

def start_new_chat():
    """Clear current chat messages"""
    st.session_state.messages = []
