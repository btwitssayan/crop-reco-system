import joblib 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the model, scaler, and encoder
model = joblib.load('D:/crop/trained_model.joblib')
scaler = joblib.load('D:/crop/feature_scaler.joblib')
encoder = joblib.load('D:/crop/encoder.joblib')


import warnings

# Ignore FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)
#2
# Function to get confidence level and top 5 crop recommendations
def get_crop_recommendations(features, specific_crop, model, scaler, label_encoder):
    # Scale the input features
    features_scaled = scaler.transform([features])
    
    # Predict probabilities
    probabilities = model.predict_proba(features_scaled)[0]
    
    # Get the confidence level for the specific crop
    crop_index = label_encoder.transform([specific_crop])
    confidence_level = probabilities[crop_index][0] * 100
    
    # Get the top 5 crop recommendations
    top_5_indices = np.argsort(probabilities)[-5:][::-1]
    top_5_crops = label_encoder.inverse_transform(top_5_indices)
    
    return confidence_level, list(top_5_crops)

# Example usage
features = [104	,18	,30	,23.603016,	60.396475	,6.779833	,140.937041]  # Input features (N, P, K, temperature, humidity, rainfall, pH)
specific_crop = 'coffee'

confidence, top_5_crops = get_crop_recommendations(features, specific_crop, model, scaler, encoder)

print(f"Confidence level for {specific_crop} in given conditions: {confidence:.2f}%")
print("Top 5 crop recommendations:")
for crop in top_5_crops:
    print(f"{crop}")