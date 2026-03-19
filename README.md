# 🎤 EchoMail - Voice-Based Email Assistant (Accessible AI Communication System)

A **voice-driven email assistant** designed to empower users — especially **visually impaired and physically challenged individuals** — to manage emails efficiently using **speech interaction instead of traditional input devices**.

---

## 🌟 Overview

This project is a **multi-module intelligent assistant** that integrates:

* 🎤 Speech Recognition (STT)
* 🔊 Text-to-Speech (TTS)
* 📧 Gmail API (OAuth Authentication)
* 📥 Unified Inbox (Emails + Messaging simulation)
* 🤖 AI-based Summarization & Reply Suggestions
* 🔐 Secure Email Sending (PIN verification)
* 📊 Admin Dashboard (Streamlit)
* 🐳 Docker-based Deployment

The system follows a **voice-first design philosophy**, minimizing reliance on keyboard and mouse interaction.

---

## 🎯 Problem Statement

Traditional email systems rely heavily on:

* Visual interfaces
* Keyboard input
* Complex navigation

This creates **accessibility barriers** for:

* Visually impaired users
* Physically challenged individuals
* Elderly users

👉 This project solves that by enabling **complete email interaction through voice commands**.

---

## 🚀 Features

### 🎤 Voice Interaction

* Continuous voice-based command input
* Speech-to-Text using Whisper
* Natural feedback using Text-to-Speech

### 📧 Gmail Integration

* Secure OAuth 2.0 login
* Read latest emails
* Send emails using voice

### 📥 Unified Inbox (Milestone 3)

* Combines:

  * Emails
  * WhatsApp (simulated)
  * Telegram (simulated)
* Single access point for all messages

### 🤖 AI Capabilities

* Email summarization
* Smart reply suggestions

### 🔐 Security Layer

* Voice confirmation before sending emails
* PIN-based verification system

### 📊 Admin Dashboard

* Activity tracking
* Logs monitoring
* Event metrics

### 🌍 Multi-language Support

* Basic language detection
* Extendable for multilingual voice interaction

---

## 🧠 System Architecture

```
User Voice Input
      ↓
Speech-to-Text (Whisper)
      ↓
Command Processing Engine
      ↓
-----------------------------------
| Gmail API | Inbox | AI Modules |
-----------------------------------
      ↓
Text-to-Speech Response
      ↓
User Feedback
```

---

## 🛠️ Tech Stack

| Category   | Tools Used       |
| ---------- | ---------------- |
| Language   | Python 3.10      |
| UI         | Streamlit        |
| Voice      | Whisper, pyttsx3 |
| AI         | Transformers     |
| API        | Gmail API        |
| Auth       | OAuth 2.0        |
| Deployment | Docker           |

---

## 📁 Project Structure

```
voice-email-assistant/
├── main_app.py             # Main UI (Assistant + Dashboard)
├── voice_engine.py         # STT + TTS
├── gmail_service.py        # Gmail API integration
├── unified_inbox.py        # Unified inbox logic
├── summarizer.py           # AI summarization
├── reply_engine.py         # Smart reply system
├── security.py             # PIN + confirmation
├── logger.py               # Activity logging
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the repository

```bash
git clone https://github.com/SICE_Logs/voice-email-assistant.git
cd voice-email-assistant
```

---

### 🔹 2. Create virtual environment

```bash
py -3.10 -m venv venv
venv\Scripts\Activate.ps1
```

---

### 🔹 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Add Google API Credentials

* Download `credentials.json` from Google Cloud Console
* Place it in the project root

---

### 🔹 5. Run the application

```bash
streamlit run streamlit_app.py
```

---

## 🐳 Docker Setup

### Build image:

```bash
docker build -t voice-assistant .
```

---

### Run container:

```bash
docker run -p 8501:8501 voice-assistant
```

---

### Open in browser:

```
http://localhost:8501
```

---

## ⚠️ Important Notes

* Voice features work **only in local environment**
* Docker is used for **UI + dashboard only**
* Do NOT upload:

  * `credentials.json`
  * `token.json`

---

## 🧪 Example Commands

* “Check inbox”
* “Read email”
* “Send email”
* “Suggest reply”
* “Exit”

---

## 📊 Future Enhancements

* Wake word detection (“Hey Assistant”)
* Real WhatsApp/Telegram API integration
* Offline voice processing
* Advanced multilingual support
* Mobile application version

---

## 📌 Project Status

🚧 **Final Milestone Completed (With Enhancements in Progress)**

---

## 👨‍💻 Author

**Your Name**

---

## ⭐ Acknowledgements

* Google Gmail API
* OpenAI Whisper
* HuggingFace Transformers
* Streamlit

---

## 💡 Final Note

This project is not just a technical implementation —
it is a step towards making **digital communication more inclusive and accessible**.
