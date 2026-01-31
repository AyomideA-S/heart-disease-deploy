# Heart Disease Predictor

A machine learning pipeline to predict heart disease presence based on the UCI Cleveland dataset.

## Project Structure

- `data/`: Contains raw and processed data (ignored by git).
- `notebooks/`: Jupyter notebooks for exploration and prototyping.
- `src/`: Production-ready Python scripts.
- `models/`: Serialized models (ignored by git).

## Setup

1. Clone the repo.
2. Run the app on your local machine:
    - Install dependencies: `pip install -r requirements.txt`
    - Run the API: `uvicorn src.app:app --reload`
    - Access the Streamlit app: `streamlit run src/streamlit_app.py`
3. Alternatively, use Docker Compose to run both services: `docker-compose up`
    - Access the app at `http://localhost:8501`
    - Access the API at `http://localhost:8000`

## Dataset Description

The dataset used in this project is the UCI Cleveland Heart Disease dataset, which contains various medical attributes related to heart disease. The target variable indicates the presence or absence of heart disease.

Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data)

Here's a brief description of the features:

| **Column** | **Full Name** | **Description** | **Key Values** |
| - | - | - | - |
| **`age`** | Age | Patient's age in years. | |
| **`sex`** | Sex | Biological sex of the patient. | `1` = Male<br>`0` = Female |
| **`cp`** | **Chest Pain Type** | The type of chest pain experienced. | `1` = Typical Angina<br>`2` = Atypical Angina<br>`3` = Non-anginal Pain<br>`4` = Asymptomatic |
| **`trestbps`** | Resting Blood Pressure | Blood pressure reading upon admission (mm Hg). | |
| **`chol`** | Cholesterol | Serum cholesterol in mg/dl. | |
| **`fbs`** | Fasting Blood Sugar | Whether fasting blood sugar > 120 mg/dl. | `1` = True<br>`0` = False |
| **`restecg`** | Resting ECG | Resting electrocardiographic results. | `0` = Normal<br>`1` = ST-T wave abnormality<br>`2` = Left ventricular hypertrophy |
| **`thalach`** | Max Heart Rate | Maximum heart rate achieved during the test. | |
| **`exang`** | Exercise-Induced Angina | Chest pain caused by exercise? | `1` = Yes<br>`0` = No |
| **`oldpeak`** | ST Depression | ST depression induced by exercise relative to rest (indicates heart stress). | |
| **`slope`** | **Slope** | The slope of the peak exercise ST segment. | `1` = Upsloping<br>`2` = Flat<br>`3` = Downsloping |
| **`ca`** | **Major Vessels** | Number of major vessels colored by fluoroscopy. | `0` to `3` |
| **`thal`** | **Thalassemia** | A blood disorder classification. | `3` = Normal<br>`6` = Fixed Defect<br>`7` = Reversable Defect |
| **`target`** | Diagnosis | Presence of heart disease. | `0` = No Disease<br>`1` = Disease |
