import streamlit as st
import os
from voice_engine import listen, speak
from gmail_service import read_latest_email, send_email
from unified_inbox import get_unified_inbox
from summarizer import summarize
from reply_engine import suggest_reply
from logger import log_event
from auth_gui import authenticate_google

# ----------------------------
# SESSION STATE
# ----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "status" not in st.session_state:
    st.session_state.status = "Assistant ready"

# ----------------------------
# LOGIN
# ----------------------------
def login():
    authenticate_google()
    st.session_state.logged_in = True
    st.rerun()

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:
    st.title("Assistant")

    page = st.radio("Navigate", ["Assistant", "Dashboard"])

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ----------------------------
# LOGIN PAGE
# ----------------------------
if not st.session_state.logged_in:
    st.title("Login Required")
    if st.button("Login with Google"):
        login()
    st.stop()

# ----------------------------
# ASSISTANT PAGE
# ----------------------------
if page == "Assistant":

    st.title("🎤 Assistant Workspace")

    col1, col2, col3 = st.columns(3)
    col1.metric("Status", st.session_state.status)
    col2.metric("Last Tool", "none")
    col3.metric("Flow", "Active")

    def run_voice():
        command = listen()

        if command is None:
            st.session_state.conversation.append("❌ Could not understand")
            return

        st.session_state.conversation.append(f"🧑 {command}")

        if "inbox" in command:
            inbox = get_unified_inbox()
            msg = f"You have {len(inbox)} messages"
            speak(msg)
            st.session_state.conversation.append(f"🤖 {msg}")
            log_event("Checked inbox")

        elif "read email" in command:
            email = read_latest_email()
            summary = summarize(email)
            speak(summary)
            st.session_state.conversation.append(f"🤖 {summary}")
            log_event("Read email")

        elif "send email" in command:
            speak("Say recipient")
            to = listen()
            speak("Say subject")
            subject = listen()
            speak("Say message")
            body = listen()

            send_email(to, subject, body)
            speak("Email sent")
            st.session_state.conversation.append("🤖 Email sent")
            log_event("Email sent")

        else:
            speak("Unknown command")
            st.session_state.conversation.append("🤖 Unknown command")

    if st.button("🎤 Start Voice Input"):
        run_voice()

    st.markdown("### Conversation")
    for msg in st.session_state.conversation:
        st.write(msg)

# ----------------------------
# DASHBOARD PAGE
# ----------------------------
elif page == "Dashboard":

    st.title("📊 Admin Dashboard")

    # Ensure logs file exists
    if not os.path.exists("logs.txt"):
        with open("logs.txt", "w") as f:
            f.write("System started\n")

    with open("logs.txt") as f:
        logs = f.readlines()

    st.metric("Total Events", len(logs))

    st.markdown("### Activity Logs")

    for log in logs[::-1]:
        st.write(log)