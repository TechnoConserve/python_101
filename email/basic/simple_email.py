import smtplib
import sys

from email.message import EmailMessage
from email.headerregistry import Address

from config.config_handler import get_setting

CONFIG_FILE = 'config/settings.ini'
HOST = get_setting(CONFIG_FILE, 'Auth', 'host')
USERNAME = get_setting(CONFIG_FILE, 'Auth', 'username')
PASSWORD = get_setting(CONFIG_FILE, 'Auth', 'password')


def authenticate(host, username, passwd):
    """
    Authenticated with SMTP server and return server object.
    :return: Authenticated server object.
    """
    server = smtplib.SMTP_SSL(host)
    server.set_debuglevel(1)
    server.connect(host)
    server.login(username, passwd)
    return server


def send_email(subject, body_text, emails):
    """
    Send an email then close the server connection.
    :param subject: Subject header.
    :param body_text: Body of the message.
    :param emails: Email addresses to send to. E.g. person@domain.com
    :return: None
    """
    server = authenticate(HOST, USERNAME, PASSWORD)

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = Address('Avery Uslaner', addr_spec=USERNAME)
    msg['To'] = (Address(addr_spec=email) for email in emails)
    msg.set_content(body_text)

    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    emails = ['promopennygather@gmail.com', 'admin@averyuslaner.com']
    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, emails)
