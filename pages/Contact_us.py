import streamlit as st

st.header("Contact me")

with st.form(key="Email forms"):
    input_gmail= st.text_input("Your email address")
    input_text =st.text_area("Your message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
         print("you printed button")