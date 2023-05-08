import smtplib, ssl

host = "smtp.gmail.com"
port = 465

password= "wkhiaexeauqdlhlb"
# user = "securesally@gmail.com"
user = "sanjarbek.soatov1989@gmail.com"

receiver = "sanjarbek.89.ss@gmail.com"

context = ssl.create_default_context()

message= """\
Subject:Hi!
Hi, 
How are you?
"""
with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(user, password)
    server.sendmail(user, receiver, message )