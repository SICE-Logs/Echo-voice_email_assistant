

def log_event(event):
    with open("logs.txt", "a") as f:
        f.write(event + "\n")