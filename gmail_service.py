import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_service():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build('gmail', 'v1', credentials=creds)

def read_latest_email():
    service = get_service()
    results = service.users().messages().list(userId='me', maxResults=1).execute()
    messages = results.get('messages', [])

    if not messages:
        return "No emails found."

    msg = service.users().messages().get(userId='me', id=messages[0]['id']).execute()

    headers = msg['payload']['headers']
    subject = ""
    for h in headers:
        if h['name'] == 'Subject':
            subject = h['value']

    return f"Latest email subject: {subject}"

def send_email(to, subject, body):
    service = get_service()

    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    service.users().messages().send(
        userId='me',
        body={'raw': raw}
    ).execute()

    return "Email sent successfully"