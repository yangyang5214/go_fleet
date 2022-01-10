# -*- coding: UTF-8 -*-

import smtplib
from email.message import EmailMessage

with open('/opt/email_pwd') as f:
    lines = f.readlines()
    email_user = lines[0].strip()
    email_pwd = lines[1].strip()


def send_email(send_to: str, text: str, sub_title: str):
    smtplib_ssl = smtplib.SMTP_SSL('smtp.126.com', 465)
    smtplib_ssl.login(email_user, email_pwd)

    msg = EmailMessage()
    msg['Subject'] = sub_title
    msg['From'] = email_user
    msg['To'] = send_to
    msg.set_content(text)

    smtplib_ssl.send_message(msg)
    smtplib_ssl.quit()


if __name__ == '__main__':
    send_email("beer5214@126.com", "text", "text")
