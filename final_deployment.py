import numpy as np
import pandas as pd
import streamlit as st 
import pickle 
st.title("Tesla Stock Prediction")
def input_date():
    end_date = st.text_input("Enter the Date")
    return end_date

date = input_date()
last_date = "15-03-19"

load_model = pickle.load(open(r"C:\Users\SP\Downloads\aaaaaa\model.sav","rb"))


prediction = load_model.predict(start = "15-03-19", end = date,dynamic=False)

st.write(prediction)