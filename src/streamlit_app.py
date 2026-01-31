import streamlit as st  # type: ignore
import requests  # type: ignore

API_URL = "http://127.0.0.1:8000/predict"

st.title("Heart Disease Prediction")

# Age
age = st.number_input("Age (years)", min_value=1, max_value=120, value=25)
# Sex
sex = st.selectbox("Sex", ["Male", "Female"])
sex_mapping = {"Male": 1, "Female": 0}
sex_encoded = sex_mapping[sex]
# Chest pain
cp_labels = [
    "Typical Angina",
    "Atypical Angina",
    "Non-anginal Pain",
    "Asymptomatic"
]
cp = st.selectbox("Chest Pain Type", cp_labels)
cp_mapping = dict(zip(cp_labels, range(1, len(cp_labels) + 1)))
cp_encoded = cp_mapping[cp]

# Resting blood pressure
trestbps = st.number_input(
    "Resting Blood Pressure (mmHg)",
    min_value=0,
    max_value=200,
    value=120
)
# Serum cholesterol
chol = st.number_input(
    "Serum Cholesterol (mg/dl)",
    min_value=0,
    max_value=600,
    value=200
)
# Max heart rate achieved
thalach = st.number_input(
    "Max Heart Rate Achieved (bpm)",
    min_value=0,
    max_value=250,
    value=150
)
# ST depression
oldpeak = st.number_input(
    "ST Depression (mm)",
    min_value=0.0,
    max_value=6.2,
    value=0.0
)

binary_mapping = {"Yes": 1, "No": 0}
# Fasting blood sugar > 120 mg/dl
fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    list(binary_mapping.keys())
)
fbs_encoded = binary_mapping[fbs]
# Exercise-induced angina
exang = st.selectbox("Exercise-Induced Angina", list(binary_mapping.keys()))
exang_encoded = binary_mapping[exang]

# Resting ECG
restecg_mapping = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg = st.selectbox("Resting ECG results", list(restecg_mapping.keys()))
restecg_encoded = restecg_mapping[restecg]
# Slope of peak exercise ST segment
slope_mapping = {
    "Upsloping": 1,
    "Flat": 2,
    "Downsloping": 3
}
slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    list(slope_mapping.keys())
)
slope_encoded = slope_mapping[slope]
# Thalassemia
thal_mapping = {
    "Normal": 3,
    "Fixed Defect": 6,
    "Reversible Defect": 7
}
thal = st.selectbox("Thalassemia", list(thal_mapping.keys()))
thal_encoded = thal_mapping[thal]

# Number of major vessels colored by fluoroscopy
ca = st.slider(
    "Number of Major Vessels Colored by Fluoroscopy",
    min_value=0,
    max_value=3,
    value=0
)


input_data = {
    "age": age,
    "sex": sex_encoded,
    "cp": cp_encoded,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs_encoded,
    "restecg": restecg_encoded,
    "thalach": thalach,
    "exang": exang_encoded,
    "oldpeak": oldpeak,
    "slope": slope_encoded,
    "ca": ca,
    "thal": thal_encoded
}

if st.button("Predict"):
    response = requests.post(API_URL, json=input_data)
    if response.json()["heart_disease"]:
        st.error("The model predicts high risk of heart disease.")
    else:
        st.success("The model predicts low risk.")
