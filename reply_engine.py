def suggest_reply(message):
    message = message.lower()

    if "meeting" in message:
        return "I will attend the meeting."
    elif "thanks" in message:
        return "You're welcome."
    elif "urgent" in message:
        return "I will check and respond soon."
    else:
        return "Noted. I will get back to you."