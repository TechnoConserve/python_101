import smtplib

from email.message import EmailMessage
from email.headerregistry import Address

from config.config_handler import get_setting

USERNAME = get_setting('config/settings.ini', 'Auth', 'username')
PASSWORD = get_setting('config/settings.ini', 'Auth', 'password')

HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "admin@averyuslaner.com"
FROM = "uslaner.avery@gmail.com"
text = "This is an email message."

msg = EmailMessage()
msg['Subject'] = SUBJECT
msg['From'] = Address('Avery Uslaner', addr_spec=FROM)
msg['To'] = Address('Avery Uslaner', addr_spec=TO)
msg.set_content("""\
Hello!

This is an email sent from a python script.

-Avery Uslaner
""")

server = smtplib.SMTP_SSL(HOST)
server.set_debuglevel(1)
server.connect(HOST)
server.login(USERNAME, PASSWORD)
server.send_message(msg)
server.quit()
