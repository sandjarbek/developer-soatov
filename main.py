import streamlit as st
import pandas

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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
print(df)
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])