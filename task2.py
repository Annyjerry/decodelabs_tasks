

import streamlit as st
import numpy as np
import joblib


model = joblib.load("logistic_regression_model.pkl")


st.title("Titanic Survival Prediction System")

st.write(
    "This web application predicts whether a passenger "
    "would survive the Titanic disaster using a "
    "Logistic Regression Machine Learning model."
)



st.header("Enter Passenger Details")

# Passenger Class
pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

# Gender
sex = st.selectbox(
    "Gender",
    ["male", "female"]
)

# Age
age = st.number_input(
    "Age",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

# Siblings/Spouses
sibsp = st.number_input(
    "Number of Siblings/Spouses aboard",
    min_value=0,
    max_value=10,
    value=0
)

# Parents/Children
parch = st.number_input(
    "Number of Parents/Children aboard",
    min_value=0,
    max_value=10,
    value=0
)

# Fare
fare = st.number_input(
    "Passenger Fare",
    min_value=0.0,
    value=50.0
)

# Embarked Port
embarked = st.selectbox(
    "Embarked Port",
    ["C", "Q", "S"]
)



# Encode Gender
if sex == "male":
    sex = 1
else:
    sex = 0

# Encode Embarked
embarked_mapping = {
    "C": 0,
    "Q": 1,
    "S": 2
}

embarked = embarked_mapping[embarked]


if st.button("Predict Survival"):

    # Create input array
    input_data = np.array([[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        embarked
    ]])

    # Make prediction
    prediction = model.predict(input_data)

    # Prediction probability
    probability = model.predict_proba(input_data)

    
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("Passenger Would Survive")
    else:
        st.error("Passenger Would Not Survive")

    st.subheader("Prediction Probability")

    st.write(
        f"Survival Probability: "
        f"{probability[0][1] * 100:.2f}%"
    )

    st.write(
        f"Non-Survival Probability: "
        f"{probability[0][0] * 100:.2f}%"
    )