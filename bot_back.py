# for database and api
import db
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from gemini_tone.tone import gem_tone
import re

# Import necessary LangChain components
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# to deal with gui and secret keys
import streamlit as st
from dotenv import load_dotenv
import time

load_dotenv()

# Initialize the input checker
import Checkers as input_checker
input_checker = input_checker.InputChecker()


# Initialize memory (conversation stored in memory)
memory = ConversationBufferMemory(memory_key="messages", return_messages=True)
_model = None  # Avoid clashing with Streamlit

def get_model():
    global _model
    if _model is None:
        import streamlit as st
        import asyncio
        
        # Try Streamlit secrets first, fallback to .env for local
        try:
            api_key = st.secrets["GOOGLE_API_KEY"]
        except:
            api_key = os.getenv('API_KEY')
        
        # Create event loop if it doesn't exist || to avoid RuntimeError in Streamlit
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        _model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-preview-05-20",
            temperature=0.2,
            google_api_key=api_key
        )
    return _model


# Keywords for conversation
GREETING_KEYWORDS = ["hi", "hello", "hey", "greetings", "whats up", "what's up", "yo", "how are you", "how are you doing"]
ACCEPTED_KEYWORDS = [ "offense", "offenses", "violation", "violations", "rules", "policies",
                    "rights", "responsibilities", "student rights", "classroom conduct", "dress code",
                    "discipline", "code of conduct", "sanction", "penalty", "freedom", "academic", "mcm", "mmcm"]
GOODBYE_KEYWORDS = ["thank you", "goodbye", "farewell", "thanks", "ty", "thank", "bye"]
IDENTITY_KEYWORDS = [ "what are you", "who are you", "are you a bot", "what is your name",  "what's your name",
                     "what can you do", "your purpose", "are you human",  "describe yourself", "tell me about yourself",
                     "what do you do", "what is your function", "what is your role", "what are you here for"]


# Query the LLM
def query_gemini_api(user_input):
    tone = gem_tone()
    db_content = db.extract_raw_data_from_db()

    model = get_model() # model initialization

    prompt = PromptTemplate(
        input_variables=["db_content", "user_input", "tone"],
        template="{tone} Answer the query based on the following data: {user_input}. Limit up to 500 words. Here is the data: {db_content}"
    )

    user_input = user_input.strip().lower()
    llm_chain = LLMChain(prompt=prompt, llm=model)

    # Reject dangerous or nonsensical inputs
    if any([
        input_checker.is_mathematical_expression(user_input),
        input_checker.is_nonsensical_input(user_input),
        input_checker.is_sql_injection_attempt(user_input)
    ]):
        return "I'm sorry, I can't help you with that. Please ask questions regarding the handbook. Could you please ask something else or clarify your question?"

    # Check greetings, goodbye, identity, etc.
    elif input_checker.contains_keywords(user_input, GOODBYE_KEYWORDS):
        return "You are very much welcome! I am glad I could help!"

    elif input_checker.contains_keywords(user_input, GREETING_KEYWORDS) and len(user_input) <= 17:
        return "Hello! How may I assist you today?"
    
    elif any(phrase in user_input for phrase in IDENTITY_KEYWORDS):
        return "I'm MMCMate, your AI chatbot assistant designed to help students understand Mapúa MCM’s school policies, rights, and responsibilities."

    elif user_input.strip() in {"mmcm", "mcm"}:
        return (
            "MMCM is the acronym for Mapúa Malayan Colleges Mindanao, a private educational institution in the Philippines. "
            "It is part of the Mapúa University system. If you have specific questions about MMCM, feel free to ask!"
        )

    elif (
        re.search(r"\b(what is|who.*is|tell me about)\b.*\b(mmcm|mcm)\b", user_input)
        and not input_checker.contains_keywords(user_input, ACCEPTED_KEYWORDS)
    ):
        return (
            "MMCM is the acronym for Mapúa Malayan Colleges Mindanao, a private educational institution in the Philippines. "
            "It is part of the Mapúa University system. If you have specific questions about MMCM, feel free to ask!"
        )
    
    elif input_checker.contains_keywords(user_input, ACCEPTED_KEYWORDS):
        response = llm_chain.run({"db_content": db_content, "user_input": user_input, "tone": tone})
    else:
        response = llm_chain.run({"db_content": db_content, "user_input": user_input, "tone": tone})

    if "Unavailable" in response:
        return "I'm sorry, I couldn't find an answer to your question. Could you please rephrase it or ask something else?"

    return response

# Handle conversation in-memory only
def handle_conversation():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask me anything about the school's handbook!")

    if user_input:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message immediately
        with st.chat_message("user", avatar='https://raw.githubusercontent.com/vennDiagramm/MMCMate_An_AI_Chatbot_for_School_Policy_Assistance/main/icons/user_icon.ico'):
            st.markdown(user_input)

        # Get assistant response
        result_gen = query_gemini_api(user_input)

        # Display assistant response
        with st.chat_message("assistant", avatar='https://raw.githubusercontent.com/vennDiagramm/MMCMate_An_AI_Chatbot_for_School_Policy_Assistance/main/icons/mapua_icon_83e_icon.ico'):
            assistant_message = ""
            placeholder = st.empty()
            for word in result_gen:
                assistant_message += word
                placeholder.markdown(f"<div style='text-align: justify;'>{assistant_message}</div>", unsafe_allow_html=True)
                time.sleep(0.02)

        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
