import streamlit as st
import numpy as np
import pickle

# Load the saved model
loaded_model = pickle.load(open('D:/heart_disease_model.sav', 'rb'))

# Create a function for heart disease prediction
def heart_disease(input_data):
    # Convert input_data to numeric values
    input_data_numeric = [float(x) for x in input_data]

    # Convert to numpy array and reshape
    input_data_as_numpy_array = np.asarray(input_data_numeric)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The patient is fine"
    else:
        return "The person has heart disease"

# Define the main function for Streamlit app
def main():
    # Giving a title and displaying an image
    st.image('C:/Users/HP/Downloads/heart_diseases.png')
    st.title("Heart Disease Prediction")

    # Getting the input data from the user
    age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
    sex = st.selectbox("Select your sex:", options=["Male", "Female"])
    sex = 1 if sex == "Male" else 0
    cp = st.number_input("Enter your cp value:", min_value=0, max_value=3, step=1)
    trestbps = st.number_input("Enter your trestbps value:", min_value=0)
    chol = st.number_input("Enter your chol value:", min_value=0)
    fbs = st.selectbox("Is your fbs value greater than 120 mg/dl?", options=["Yes", "No"])
    fbs = 1 if fbs == "Yes" else 0
    restecg = st.number_input("Enter your restecg value:", min_value=0, max_value=2, step=1)
    thalach = st.number_input("Enter your thalach value:", min_value=0)
    exang = st.selectbox("Do you experience exercise-induced angina?", options=["Yes", "No"])
    exang = 1 if exang == "Yes" else 0
    oldpeak = st.number_input("Enter your oldpeak value:", min_value=0.0, format="%.1f")
    slope = st.number_input("Enter your slope value:", min_value=0, max_value=2, step=1)
    ca = st.number_input("Enter your ca value:", min_value=0, max_value=4, step=1)
    thal = st.number_input("Enter your thal value:", min_value=0, max_value=3, step=1)

    # Code for prediction
    result = ""

    # Creating a button with custom color
    if st.button('Result'):
        result = heart_disease([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        st.success(result)

if __name__ == '__main__':
    main()
