import streamlit as  st
import joblib 
import sklearn
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.model_selection import train_test_split
st.header('Social Network Predict purchased or not')
number1=st.number_input('input the Estimatedsalary:',min_value=0,max_value=20000000000,placeholder='enter estimated salary')
number2=st.number_input('input the age:',min_value=0,max_value=100,placeholder='enter age')

path=r'C:\Users\bhand\Downloads\logic (1).pkl'
model=joblib.load(path)

if st.button("predict"):
    test=model.predict([[number1,number2]])
    if test==1:
        st.status("Purchased",state="complete")
    elif test!=1:
        st.status("cannot purchase",state='complete')


   

