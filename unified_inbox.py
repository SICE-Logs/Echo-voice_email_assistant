import datetime
from gmail_service import get_service
import base64

# -----------------------------
# FETCH EMAILS FROM GMAIL
# -----------------------------

def fetch_emails(max_results=5):
    service = get_service()

    results = service.users().messages().list(
        userId='me',
        maxResults=max_results
    ).execute()

    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        message = service.users().messages().get(
            userId='me',
            id=msg['id']
        ).execute()

        headers = message['payload']['headers']

        subject = ""
        sender = ""

        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']
            if h['name'] == 'From':
                sender = h['value']

        email_list.append({
            "platform": "Email",
            "sender": sender,
            "content": subject,
            "time": "Recent"
        })

    return email_list


# -----------------------------
# SIMULATED WHATSAPP / TELEGRAM
# -----------------------------

def fetch_messages():
    # Dummy dataset (Milestone 3 requirement)
    messages = [
        {
            "platform": "WhatsApp",
            "sender": "Rahul",
            "content": "Meeting at 5 PM today",
            "time": str(datetime.datetime.now())
        },
        {
            "platform": "Telegram",
            "sender": "Team Group",
            "content": "Project submission deadline tomorrow",
            "time": str(datetime.datetime.now())
        }
    ]

    return messages


# -----------------------------
# UNIFIED INBOX
# -----------------------------

def get_unified_inbox():
    emails = fetch_emails()
    messages = fetch_messages()

    unified = emails + messages

    # Sort by time if needed (basic version keeps order)
    return unified


# -----------------------------
# DISPLAY FUNCTION
# -----------------------------

def display_inbox():
    inbox = get_unified_inbox()

    print("\n===== UNIFIED INBOX =====\n")

    for i, item in enumerate(inbox, 1):
        print(f"{i}. [{item['platform']}] {item['sender']}")
        print(f"   {item['content']}")
        print("-" * 40)

    return inbox