import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\Soatov_S.png", width=300)


with col2:
    st.title("Soatov Sanjar Sarvarovich")
    content="""Senior teacher of "Customs regulation and customs payments" department of Customs Institute 
He teaches Customs statistics and system analysis at the Customs Institute """
    st.info(content)


content2= """Bellow you can find some of the apps I have build in Python. Feel free to contact me!"""
st.write(content2)