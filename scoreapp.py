import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("Custom Model Training App")
st.write("""
### Train a Linear Regression Model with Custom Columns
""")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("File Uploaded Successfully!")
    
    st.write(data.head())
    
    columns = data.columns.tolist()
    st.write("Select the feature column (independent variable):")
    feature_column = st.selectbox("Feature Column", columns)
    
    st.write("Select the target column (dependent variable):")
    target_column = st.selectbox("Target Column", columns)
    
    model = None

    if st.button("Train Model"):
        X = data[[feature_column]]
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        test_score = model.predict(X_test)
        st.write(f"Test Score (Sample): {test_score[0]}")
        
        st.write("Model trained successfully!")

        st.session_state["model"] = model

    input_value = st.number_input(f"Enter the value in {feature_column}", value=0.0)

    if st.button("predict"):
        if "model" in st.session_state:
            prediction = st.session_state["model"].predict([[input_value]])
            st.write(f"Predicted Value: {prediction[0]}")
        else:
            st.write("Please train the model first.")
else:
    st.write("Please upload a CSV file to proceed.")

st.markdown("""
<a href="https://www.linkedin.com/in/prakash-bhandari-23559b334/" target="_blank">
<img src="https://i.imgur.com/3aLajp0.png" alt="prakass" style="height: 24px; width: 24px;">
prakass
</a>
""", unsafe_allow_html=True)
