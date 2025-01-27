import streamlit as st
import joblib
st.title("Diabetes Prediction")
st.write("### Predict whether a person has diabetes based on medical data.")
path=r'C:\Users\bhand\Downloads\diabetic100.pkl'
model=joblib.load(path)



blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=0)


bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=0.0, step=0.1)

age = st.number_input("Age", min_value=0, max_value=120, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=0)
if st.button("Predict"):
   
 if (blood_pressure and bmi and age and glucose):

   prediction=model.predict([[blood_pressure,bmi,age,glucose]])
   if prediction == 1:
        st.write("The model predicts that this person **has diabetes**.")
   else:
        st.write("The model predicts that this person **does not have diabetes**.")
 else:
    st.write("fill the above details")