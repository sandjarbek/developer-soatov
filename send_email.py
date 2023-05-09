import smtplib, ssl
import os

# if (os.environ.get("DB_TYPE") == None):
#  from dotenv import load_dotenv
#  from config.definitions import ROOT_DIR
#  load_dotenv(os.path.join(ROOT_DIR, 'config', 'conf', '.env'))
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("PASSWORD")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv("PASSWORD")
    # user = "securesally@gmail.com"
    user = "sanjarbek.soatov1989@gmail.com"
    receiver = "sanjarbek.89.ss@gmail.com"
    context = ssl.create_default_context()



    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)



# send_email(message)

if __name__=='__main__':
    print(password)
