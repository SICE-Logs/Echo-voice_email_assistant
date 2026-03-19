USER_PIN = "7097"

def confirm_action():
    confirm = input("Confirm (yes/no): ")
    return confirm.lower() == "yes"

def verify_pin():
    pin = input("Enter PIN: ")
    return pin == USER_PIN