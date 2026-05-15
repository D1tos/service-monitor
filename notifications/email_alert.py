import os
import logging
import smtplib

from email.message import EmailMessage

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

email_enabled = bool(
    EMAIL_SENDER and
    EMAIL_PASSWORD and
    EMAIL_RECEIVER
)


def send_email(subject, body):
    if not email_enabled:
        logging.warning("Email alerts disabled")
        return

    message = EmailMessage()

    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()

            server.login(
                EMAIL_SENDER,
                EMAIL_PASSWORD
            )
            server.send_message(message)

        logging.info("Email alert sent")

    except Exception as e:
        logging.error(f"Email ERROR: {e}")