# Import our packages
import streamlit as st
import joblib
import os
import numpy as np

attribute = ("""

## Attribute Information

**Age**: Age in years, which is an important factor in assessing the risk of heart disease.

**Sex**: Sex of the user, where 1 represents male and 0 represents female.

**Gender**: an important risk factor for heart disease.

**CP**: Chest pain type, which is a categorical variable with four possible values. 
- Value 1 represents typical angina
- Value 2 represents atypical angina
- Value 3 represents non-anginal pain
- Value 4 represents asymptomatic

**Trestbps**: Resting blood pressure in mm Hg on admission to the hospital. 
High blood pressure is a significant risk factor for heart disease.

**Chol**: Serum cholesterol level in mg/dl. 

**Fbs**: Fasting blood sugar in mg/dl, where a value of 1 indicates 
a fasting blood sugar level greater than 120 mg/dl.
High blood sugar levels are associated with an increased risk of heart disease
- 0 = false
- 1 = true

**Restecg**: Resting electrocardiographic results, which is a categorical variable with 
three possible values. 
- Value 0 represents normal results
- Value 1 represents ST-T wave abnormality 
- Value 2 represents probable or definite left ventricular hypertrophy

**Thalach**: Maximum heart rate achieved during exercise, which is an important indicator of heart health.

**Exang**: Exercise-induced angina where:
- a value of 1 indicates that the user experiences angina during exercise 
- a value of 0 indicates no angina is a common symptom of heart disease

**Oldpeak**: ST depression induced by exercise relative to rest, which is 
another important indicator of heart health.

**Slope**: The slope of the peak exercise ST segment, which 
is a categorical variable with three possible values. 
- Value 1 represents upsloping
- Value 2 represents flat
- Value 3 represents downsloping.

**Ca**: Number of major vessels (0-3) colored by flourosopy, 
which is an important measure of heart disease severity.

**Thal**: A categorical variable with three possible values. 
- Value 3 represents normal results
- Value 6 represents fixed defect
- Value 7 represents reversible defect

**Num**: A diagnosis of heart disease (angiographic disease status), 
which is a binary variable 
- Value of 0 indicating less than 50% diameter narrowing 
- Value of 1 indicating greater than 50% diameter narrowing.

""")

encoded_values = {"Female": 0, "Male": 1, 'typical angina': 0, 'atypical angina': 1, "non-anginal pain": 2,
                  "asymptomatic": 3,
                  "lower than 120mg/ml": 0, "greater than 120mg/ml": 1, 'normal': 0, 'ST-T wave abnormality': 1,
                  'left ventricular hypertrophy': 2, "no": 0, "yes": 1, "upsloping": 0, "flat": 1, "downsloping": 2,
                  "normal": 1,
                  "fixed defect": 2, "reversable defect": 3}


# Function for encoding
def a(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value


def ml():
    st.header("Our Prediction Process")
    st.write("""The Prediction Page of this WebApp asks users to provide key medical information such as age, 
gender, blood pressure, cholesterol levels, and other relevant factors that may contribute to 
heart disease. Based on this information, the WebApp uses machine learning algorithms to predict 
the likelihood of the user developing heart disease.
		
The machine learning algorithms used in this WebApp are trained on a dataset obtained from
https://archive.ics.uci.edu/ml/datasets/heart+disease, which is a reliable source for heart 
disease data. By analyzing this data and identifying patterns, the algorithms can predict the 
user's risk level for heart disease with a high degree of accuracy.""")

    st.markdown(attribute)

    st.header("Input Values that are Needed")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Enter your Age", 29, 80, 54)
        chest_pain_type = st.selectbox("Your Chest pain type", ['typical angina', 'atypical angina', "non-anginal pain",
                                                                "asymptomatic"])
        cholestrol = st.number_input("Cholesterol Value", 120, 575, 245)
        rest_ecg = st.selectbox("Your Rest ECG type",
                                ['normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'])
        exercise_induced_angina = st.radio("Exercise Induced Angina", ["yes", "no"])
        st_slope = st.selectbox("Your ST Slope type", ['upsloping', 'flat', 'downsloping'])

    with col2:
        sex = st.radio("What is your Gender", ["Male", "Female"])
        resting_blood_pressure = st.number_input("Resting Blood Pressure value", 90, 200, 131)
        fasting_blood_sugar = st.radio("Your Fasting blood sugar value is",
                                       ["lower than 120mg/ml", 'greater than 120mg/ml'])
        max_heart_rate_achieved = st.number_input("Your maximum heart rate achieved value", 70, 210, 109)
        st_depression = st.number_input("Your ST depression value", 0.0, 7.0, 1.0, step=0.1)
        num_major_vessels = st.number_input("How many major vessels do you have?", 0, 3, 1)

    thalassemia = st.selectbox("Your Thalassemia type", ["normal", "fixed defect", "reversable defect"])

    with st.expander("Your selected options"):
        so = {"age": age,
              "sex": sex, "chest_pain_type": chest_pain_type, "resting_blood_pressure": resting_blood_pressure,
              "cholestrol": cholestrol, "fasting_blood_sugar": fasting_blood_sugar, "rest_ecg": rest_ecg,
              "max_heart_rate_achieved": max_heart_rate_achieved, "exercise_induced_angina": exercise_induced_angina,
              "st_depression": st_depression, "st_slope": st_slope, "num_major_vessels": num_major_vessels,
              "thalassemia": thalassemia}

        st.write(so)

        result = []

        for i in so.values():
            if type(i) == int or type(i) == float:
                result.append(i)

            else:
                res = a(i, encoded_values)
                result.append(res)

    # st.write(result)

    with st.expander("Prediction Results"):

        input = np.array(result).reshape(1, -1)
        # st.write(input)

        m = joblib.load("lr_model")

        prediction = m.predict(input)
        st.write(prediction)

        prob = m.predict_proba(input)
        # st.write(prob)

        if prediction == 1:
            st.warning("Positive Risk!!! Be Careful")
            prob_score = {"Positive Risk": prob[0][1],
                          "Negative Risk": prob[0][0]}
            st.write(prob_score)

        else:
            st.success("Negative Risk!!! Enjoy!!")
            prob_score = {"Negative Risk": prob[0][0],
                          "Positive Risk": prob[0][1]}
            st.write(prob_score)
