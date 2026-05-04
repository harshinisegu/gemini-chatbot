# 🤖 Gemini AI Chatbot

An interactive AI chatbot built using the Google Gemini API and Streamlit, designed to deliver real-time, context-aware responses with a smooth user experience.

---

## 🚀 Features

- 💬 Real-time conversational AI responses  
- 🔄 Streaming output for better UX  
- 🧠 Context-aware chat with session memory  
- 📜 Chat history persistence  
- 🔐 Secure API key management using environment variables  
- ⚡ Dynamic model selection (Gemini variants)  
- 🎨 Simple and interactive UI with Streamlit  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Google Gemini API  
- python-dotenv  

---

## 📂 Project Structure
├── app.py # Main Streamlit application
├── .env # Environment variables (API key)
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up Environment Variables

Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here
▶️ Run the Application
streamlit run app.py

🧠 How It Works

- The chatbot uses the Google Gemini API to generate intelligent responses based on user input.
- Streamlit manages the frontend interface, while session state ensures conversation continuity and history tracking.

🔒 Security
- API keys are stored securely using .env files
- No sensitive data is exposed in the codebase
📈 Future Improvements
- Add multi-user authentication
- Deploy using cloud platforms (AWS / GCP / Azure)
- Enhance UI/UX with advanced components
- Integrate voice-based interaction

