import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')

name=st.text_input("Enter your name: ")

age=st.slider("Select your age: ",0,100,25)

st.write(f"Your age is {age}.")

options=['Python','Java','C','JavaScript']
choice=st.selectbox("Choose your favourite language: ",options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data={
    "Name":['Dhrupad','Dhruv','Mithila','John'],
    "Age":[23,32,27,29],
    "City":['Kolkata','Bangalore','Pune','Chicago']
}

df=pd.DataFrame(data)

upload_file=st.file_uploader("Choose a CSV file",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)