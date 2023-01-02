import os
from dotenv import load_dotenv
from email.message import EmailMessage  # This is pre-installed with Python
import ssl  # Pre-installed
import smtplib  # Pre-installed

load_dotenv()

email_sender: str = os.getenv("EMAIL_SENDER")
email_password: str = os.getenv("EMAIL_PW")
email_receiver: str = "mivifov214@letpays.com"
subject: str = "This is the subject"
body: str = """
This is the description and body of the email
"""

em: EmailMessage = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context: ssl.SSLContext = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
