import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="Email forms"):
    user_gmail= st.text_input("Your email address")
    message =st.text_area("Your message")
    message=message+"\n"+user_gmail
    button = st.form_submit_button("Submit")

    if button:
         send_email(message, user_gmail)