import email 
import ssl 
import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import Config

sender = os.environ['email']
password = os.environ['password']
subject = "Pokemon Draft Generation"
body = """Hello there, \nIt seems you have requested a draft of Pokemon.\nAttached to this file hould be a csv file containing the list.\nHave a good day,\nServiux"""

message = MIMEMultipart()
message["From"] = sender
message["To"] = Config.EMAIL
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

with open(Config.OUT_FILE, "rb") as attachment:
  part = MIMEBase("application", "octet-stream")
  part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    f"attachment; filename= {Config.OUT_FILE}",
)

message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
  server.login(sender, password)
  server.sendmail(sender, Config.EMAIL, text)






