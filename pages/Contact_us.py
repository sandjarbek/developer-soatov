import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email forms"):
    user_gmail= st.text_input("Your email address")
    raw_message =st.text_area("Your message")
    message=f"""\
Subject: New eamil from {user_gmail}
From {user_gmail}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    print(button)

    if button:
         send_email(message)
         st.info("Your email was send successfully")