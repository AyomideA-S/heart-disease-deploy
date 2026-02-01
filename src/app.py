from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from joblib import load  # type: ignore
import pandas as pd  # type: ignore

# List of columns exactly as they appeared during training
model_columns = [
    "age",
    "sex",
    "trestbps",
    "chol",
    "fbs",
    "thalach",
    "exang",
    "oldpeak",
    "ca",
    "cp_2",
    "cp_3",
    "cp_4",
    "restecg_1",
    "restecg_2",
    "slope_2",
    "slope_3",
    "thal_6",
    "thal_7",
]

map_columns = {
    "cp": {2: "cp_2", 3: "cp_3", 4: "cp_4"},
    "restecg": {1: "restecg_1", 2: "restecg_2"},
    "slope": {2: "slope_2", 3: "slope_3"},
    "thal": {6: "thal_6", 7: "thal_7"},
}

app = FastAPI()
model = load("models/heart_disease_model.joblib")
scaler = load("models/scaler.joblib")

# Allow connections from anywhere (for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, we'd list specific domains here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """A simple health check endpoint."""
    return {"status": "alive"}


class HeartDiseaseInput(BaseModel):
    """Input data model for heart disease prediction.

    Attributes:
        BaseModel (BaseModel): Pydantic BaseModel for data validation.
        age (float): Age of the patient.
        sex (int): Sex of the patient (1 for male, 0 for female).
        cp (int): Chest pain type (1-4).
        trestbps (float): Resting blood pressure (mmHg).
        chol (float): Serum cholesterol (mg/dl).
        fbs (int): Fasting blood sugar > 120 mg/dl (1 or 0).
        restecg (int): Resting electrocardiographic results (0-2).
        thalach (float): Maximum heart rate achieved.
        exang (int): Exercise-induced angina (1 or 0).
        oldpeak (float): ST depression induced by exercise relative to rest.
        slope (int): Slope of the peak exercise ST segment (1-3).
        ca (int): Number of major vessels colored by fluoroscopy.
        thal (int): Thalassemia (3-7).
    """
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


def map_dummies(df: pd.DataFrame) -> pd.DataFrame:
    """Map categorical columns to their dummy variable columns.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with dummy variables mapped.
    """
    for col in map_columns.keys():
        if df[col].map(map_columns[col]).isnull().all():
            continue
        df_col = df[col].map(map_columns[col])
        df[df_col] = True
    return df


@app.post("/predict")
async def predict(data: HeartDiseaseInput):
    """
    Predict heart disease presence based on input features.

    :param data: Input data for prediction.
    :type data: HeartDiseaseInput
    :return: Prediction result indicating presence of heart disease.
    :rtype: dict
    """
    input_df = pd.DataFrame([data.model_dump()])
    input_df = map_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=False)

    features_scaled = scaler.transform(input_df)
    prediction = model.predict(features_scaled)

    return {"heart_disease": int(prediction[0])}
