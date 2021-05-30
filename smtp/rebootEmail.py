import smtplib, ssl, csv, sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIP=s.getsockname()[0]
s.close()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "notifications@hackmypi.com"
receiver_email = ("mwagner@hackmypi.com", "mwagner@hackmypi.com")
password = "ljupuwlwdcwgqwsi"
message = """Subject: OMNI Online

Testing email notifications from OMNI {ip}."""

context = ssl.create_default_context()

for rec in receiver_email:

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, rec, message.format(ip=myIP))
