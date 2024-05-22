import joblib 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import warnings

# Ignore FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the model, scaler, and encoder
model = joblib.load('D:/crop/trained_model.joblib')
scaler = joblib.load('D:/crop/feature_scaler.joblib')
encoder = joblib.load('D:/crop/encoder.joblib')

df = pd.read_csv('Crop_recommendation.csv')

def get_ideal_surroundings(crop_name, dataframe):
    crop_data = dataframe[dataframe['label'] == crop_name]
    crop_data = crop_data.drop("label",axis=1)
    if crop_data.empty:
        return f"Crop {crop_name} not found in the dataset."
    
    ideal_surroundings = crop_data.mean()
    return ideal_surroundings

crop = 'rice'
result = get_ideal_surroundings(crop, df)

print(f"For growing {crop} :")
print(f"Nitrogen: {round(result[0])}, Phosphorus: {round(result[1])}, Potassium: {round(result[2])}, Temperature: {round(result[3])}, Humidity: {round(result[4])}, PH Level: {round(result[5])}, Rainfall: {round(result[6])}")