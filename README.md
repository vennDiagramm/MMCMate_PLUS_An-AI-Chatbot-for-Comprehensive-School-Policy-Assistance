# 📚 MMCMate+ – AI Chatbot for Comprehensive School Policy Assistance 🤖

Welcome to the repository for **MMCMate+**, an upgraded AI-powered chatbot designed to assist students, teachers, and administrators of **Mapúa Malayan Colleges Mindanao (Mapúa MCM)** in navigating school policies, rules, and institutional guidelines. This project was developed as part of our **CS140-1: Software Engineering 1** course.

MMCMate PLUS builds upon the foundation of the original MMCMate, integrating enhanced backend logic and modular architecture for improved performance and maintainability.

---

🧠 **Technologies Used**

- **Python** – Core programming language for backend logic and chatbot functionality  
- **LangChain + Google GenAI (Gemini)** – Enables advanced natural language understanding and contextual responses  
- **Streamlit** – Framework for building the browser-based interactive interface  
- **NLTK, langdetect, uuid** – Utility libraries for NLP, language detection, and session management  
- **FuzzyWuzzy** – Supports fuzzy string matching for more forgiving user inputs  
- **Custom Modules** – Includes dedicated files for database handling, input validation, and session management

---

✨ **Features**

- **Policy Query Assistance** – Provides accurate, AI-generated responses about Mapúa MCM’s school policies and regulations  
- **Interactive Chat Interface** – Simple and intuitive web-based chat for quick access to information  
- **Session Management** – Saves and tracks ongoing conversations for contextual responses  
- **Smart Input Handling** – Detects and manages irrelevant or nonsensical inputs gracefully  
- **Multilingual Support** – Understands English, Filipino, and other detected languages  
- **Modular Architecture** – Organized into backend, frontend, and utility scripts for scalability  
- **.env Integration** – Uses environment variables to store API keys securely  

---

🚀 **Installation Guide**

### 1️⃣ Create and Activate a Virtual Environment
```bash
# Create a new virtual environment
python -m venv mmcmate_plus

# Activate the environment
# Windows
file_path\mmcmate_plus\Scripts\activate
# macOS/Linux
source mmcmate_plus/bin/activate
```

### 2️⃣ Install Required Packages
```bash
# (Optional) create a cache folder for faster installations
mkdir .pip_cache

# Install dependencies
pip install --cache-dir=.pip_cache -r requirements.txt
```

If installation fails for certain libraries (e.g., google-genai), try:
```bash
pip install -U langchain-google-genai
```

### 3️⃣ Set Up API Key
Since the repository is public:
1. Create a `.env` file in the project directory.  
2. Inside `.env`, paste your Gemini API key:
   ```bash
   API_KEY="your-api-key"
   ```
3. (Optional) Fix interpreter issues in VS Code:
   - Press `Ctrl + Shift + P`
   - Type **Python: Select Interpreter**
   - Choose your virtual environment (e.g., `mmcmate_plus\Scripts\python.exe`)

### 4️⃣ Run the App
```bash
streamlit run bot_front.py
```

---

**Check out our App!**
- [**mmcmate2025**](https://mmcmate2025.streamlit.app/)
- *`Note: Wake it up if it's sleeping!`*

**Admin Panel Repository**
- [MMCMate-Management-Site](https://github.com/Joooban/MMCMate-Management-Site)

---

👩‍💻 **Authors**
- **Marga Pilapil** – [@vennDiagramm](https://github.com/vennDiagramm)  
- **Jhouvann Morden** – [@Joooban](https://github.com/Joooban)  
- **Mel Macabenta** – [@Lumeru](https://github.com/Lumeru)

---

📬 **Contact & Acknowledgments**

This chatbot was developed by students of **Mapúa Malayan Colleges Mindanao (MMCM)** for academic purposes under **CS140-1: Software Engineering 1**.  
Special thanks to our instructor, as well as the **Gemini**, **LangChain**, and **Streamlit** communities for their invaluable tools and documentation.
