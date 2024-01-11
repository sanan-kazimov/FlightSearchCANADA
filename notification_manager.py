""" This class is responsible for SENDING NOTIFICATIONS with the deal flight details. """

import os
import smtplib

SENDER = os.environ["MAIL_SENDER_EMAIL"]
RECEIVER = os.environ["MAIL_RECEIVER_EMAIL"]
SENDER_PASSWORD = os.environ["MAIL_SENDER_PASSWORD"]
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


class NotificationManager:

    def __init__(self):
        pass

    def send_email(self, message):
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER,
                to_addrs=RECEIVER,
                msg=f"Subject: Ticket price decreased\n\n{message}".encode()
            )

            # Prints if successfully sent.
            print(message)
