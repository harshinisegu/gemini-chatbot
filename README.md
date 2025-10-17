````markdown
# 🤖 Gemini Chatbot (Streamlit + Google Gemini API)

A fully functional chatbot web application built using **Streamlit** and **Google’s Gemini API** (via the official `google-genai` SDK).  
This project allows users to interact with Google’s Gemini models in real time, customize system prompts, and adjust creativity—all through a clean, intuitive web interface.

---

## 🚀 Features

- 💬 **Real-time streaming** chat with Gemini 2.5 models
- ⚙️ **Customizable settings**
  - Select between `gemini-2.5-flash` (fast & efficient) and `gemini-2.5-pro` (more capable)
  - Adjust model **temperature** (creativity)
  - Define custom **system instructions** to change chatbot tone and behavior
- 🧠 **Session memory**: Keeps chat history until manually reset
- 🛡️ **Error-handling**: Recovers from client closure or rerun issues automatically
- 🔒 **Secure** API key management using `.env`
- 🖥️ **Simple UI** powered by Streamlit

---

## 📦 Requirements

- **Python**: 3.10, 3.11, or 3.12 (⚠️ Python 3.13 not yet fully supported)
- **Dependencies**:
  - `streamlit`
  - `google-genai`
  - `python-dotenv`

---

## 🧩 Setup Guide

### 1️⃣ Create a Project Folder

```bash
mkdir gemini-chatbot
cd gemini-chatbot
````

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
# Activate on Windows
.venv\Scripts\activate
# Activate on macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit google-genai python-dotenv
```

### 4️⃣ Create a `.env` File

In your project folder, create a file named `.env` and add your Gemini API key:

```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

You can generate your key from [**Google AI Studio**](https://aistudio.google.com/app/apikey).

### 5️⃣ Add the Application Code

Create a new file called `app.py` and paste in the full chatbot code (the error-free version that includes streaming and client caching).

Your folder structure should now look like:

```
gemini-chatbot/
│
├── .env
├── app.py
└── .venv/
```

---

## ▶️ Running the Chatbot

Launch the Streamlit app:

```bash
streamlit run app.py
```

After running, Streamlit will show a message like:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

Click the link or open it in your browser manually.
You’ll now see your chatbot interface!

---

## 💡 How to Use

1. **Type a message** in the input box at the bottom.
2. The Gemini model will **stream its response live**.
3. Use the **sidebar** to:

   * Switch between models (`flash` or `pro`)
   * Adjust **creativity** via temperature
   * Edit the **system instruction** to change tone (e.g., “You are a polite tutor”)
4. Click **🔄 Reset Chat** to start a new conversation.

---

## ⚙️ Configuration Details

| Setting                | Description                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| **Model**              | Choose the Gemini model variant. `gemini-2.5-flash` is faster, `gemini-2.5-pro` is stronger. |
| **System Instruction** | Customizes how the chatbot behaves (e.g., helpful, formal, humorous).                        |
| **Temperature**        | Controls randomness. `0.0` = factual and consistent, `1.0` = balanced, `>1.0` = creative.    |

---

## 🧰 File Structure

```
gemini-chatbot/
│
├── .env                  # Stores your Gemini API key
├── app.py                # Main Streamlit app file
├── requirements.txt       # Optional: project dependencies
└── README.md              # Documentation (this file)
```

Example `requirements.txt`:

```
streamlit
google-genai
python-dotenv
```

---

## 🧠 Troubleshooting

### ❗ RuntimeError: “Cannot send a request, as the client has been closed”

✅ Fixed in this version (client caching added).
If it still occurs, downgrade to **Python 3.12** or **3.11**.

### ❗ “No API key found”

Make sure your `.env` file exists in the project folder and contains:

```
GEMINI_API_KEY=your_key_here
```

### ❗ Port already in use

Run Streamlit on another port:

```bash
streamlit run app.py --server.port 8502
```

---

## 💬 Example System Prompts

| Role                | Example Prompt                                                   |
| ------------------- | ---------------------------------------------------------------- |
| Teacher             | “You are a patient tutor. Explain everything step-by-step.”      |
| Developer Assistant | “You are a concise coding helper. Provide examples.”             |
| Creative Writer     | “You are a storyteller who writes in a friendly, engaging tone.” |

---

## 🌐 Deployment

### 🔸 Streamlit Community Cloud (Free & Simple)

1. Push your project to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io).
3. Select your repo and deploy.
4. Add your API key under **Secrets** →

   ```
   GEMINI_API_KEY="your_key_here"
   ```

### 🔸 Other Hosting Options

* [Render](https://render.com)
* [Railway](https://railway.app)
* Self-host on VPS or cloud servers (set environment variables securely).

---

## 🧾 License

MIT License © 2025 Your Name
You’re free to use, modify, and distribute this project for personal or commercial purposes.

---

## 🥇 Credits

Built with:

* [Streamlit](https://streamlit.io)
* [Google Gemini API](https://aistudio.google.com/)
* [google-genai Python SDK](https://pypi.org/project/google-genai/)

---

**Made with ❤️ using Streamlit and Gemini.**

```
```
