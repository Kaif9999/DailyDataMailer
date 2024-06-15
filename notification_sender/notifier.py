import smtplib
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, from_email, password, smtp_server='smtp.example.com', smtp_port=465):
        self.from_email = from_email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, body, to_email):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.from_email
        msg['To'] = to_email
        
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.from_email, self.password)
            server.sendmail(self.from_email, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
