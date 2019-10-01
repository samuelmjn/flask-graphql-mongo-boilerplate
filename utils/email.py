import smtplib
from typing import Union

from constants import CONFIGS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_confirmation_email(receiver_address, uuid_to_check) -> Union[
    str, Exception]:
    """
    Send a confirmation email through SMTP on registration
    :param receiver_address:
    :param uuid_to_check:
    :returns:
    """
    return _send_email(receiver_address,
                       "Auth - Confirm your account",
                       "{}/user/confirm?uniqid={}&email={}".format(
                           CONFIGS.get("APP_URL"), uuid_to_check,
                           receiver_address))


def _send_email(to_address, topic, mail_content) -> Union[str, Exception]:
    try:
        sender = "{}@mail.com".format(CONFIGS.get("EMAIL_ACCOUNT"))
        message = MIMEMultipart()
        message["from"] = sender
        message["to"] = to_address
        message["subject"] = topic
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, "plain"))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP("smtp.mailtrap.io", 587)
        session.starttls()
        session.login(CONFIGS.get("EMAIL_ACCOUNT"),
                      CONFIGS.get("EMAIL_PASSWORD"))
        text = message.as_string()
        session.sendmail(sender, to_address, text)
        session.quit()
        return "Email has been sent."
    except Exception as exception:
        return exception
