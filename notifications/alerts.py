from notifications.telegram import send_telegram_message
from notifications.email_alert import send_email

def send_alert(message, no_telegram):
    if not no_telegram:
        send_telegram_message(message)

    send_email(
        subject="Service Monitor Alert",
        body=message
    )