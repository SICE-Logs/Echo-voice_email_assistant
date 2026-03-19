import tkinter as tk
from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_google():
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)
    
    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return True


def launch_login(on_success):

    login_window = tk.Toplevel()
    login_window.title("Login with Google")
    login_window.geometry("400x250")

    label = tk.Label(login_window, text="Login Required", font=("Arial", 16))
    label.pack(pady=20)

    def handle_login():
        status.config(text="Opening browser for login...")
        login_window.update()

        try:
            authenticate_google()
            status.config(text="Login Successful")
            login_window.destroy()
            on_success()
        except Exception as e:
            status.config(text="Login Failed")

    login_btn = tk.Button(
        login_window,
        text="Login with Google",
        command=handle_login,
        bg="#4285F4",
        fg="white",
        font=("Arial", 12)
    )
    login_btn.pack(pady=10)

    status = tk.Label(login_window, text="")
    status.pack(pady=10)