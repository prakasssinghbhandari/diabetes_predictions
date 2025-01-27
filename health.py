import streamlit as st 
import joblib
st.header("Check your Health:")
num1=st.number_input("Enter your BMI:")
num2=st.selectbox("Do you smoke",options=["Yes","No"])
num2=1 if num2=="Yes"else 0
num3=st.selectbox("do you Drink",options=["Yes","No"])
num3=1 if num3=="Yes" else 0
path=r'C:\Users\bhand\Downloads\check_diabetic.pkl'
model=joblib.load(path)

if st.button("check"):
  predict=model.predict([[num1,num2,num3]])
  st.status(f"{predict}",state="complete")