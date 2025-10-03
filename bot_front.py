import bot_back as back
from chat_session import init_chat, add_message, display_chat, start_new_chat
import streamlit as st

def main():
    st.set_page_config(
        page_title="MMCMate",
        page_icon="https://raw.githubusercontent.com/vennDiagramm/MMCMate_An_AI_Chatbot_for_School_Policy_Assistance/main/icons/mapua_icon_83e_icon.ico"
    )
    
    st.title("MMCMate :books:")
    st.write("Hello, how may I help you?")

    # Initialize in-memory chat
    init_chat()

    # Path to the database
    # db_path = os.path.join("database", "databasefinalnjud.db")

    # --- New Chat Button ---
    if st.button("🆕 New Chat"):
        start_new_chat()
        st.rerun()

    # --- Display current chat ---
    display_chat()

    # --- Handle new messages ---
    back.handle_conversation()

if __name__ == "__main__":
    main()
