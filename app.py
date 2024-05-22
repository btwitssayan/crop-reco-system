import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Crop_recommendation.csv')

# Load the model, scaler, and encoder
model = joblib.load('trained_model.joblib')
scaler = joblib.load('feature_scaler.joblib')
encoder = joblib.load('encoder.joblib')

def get_ideal_surroundings(crop_name, dataframe):
    crop_data = dataframe[dataframe['label'] == crop_name]
    crop_data = crop_data.drop("label", axis=1)
    if crop_data.empty:
        return None
    
    ideal_surroundings = crop_data.mean()
    return ideal_surroundings.to_dict()  # Convert Series to dictionary

def get_crop_recommendations(features, model, scaler, label_encoder):
    # Scale the input features
    features_scaled = scaler.transform([features])
    
    # Predict probabilities
    probabilities = model.predict_proba(features_scaled)[0]
    
    # Get the top 5 crop recommendations
    top_5_indices = np.argsort(probabilities)[-5:][::-1]
    top_5_crops = label_encoder.inverse_transform(top_5_indices)
    
    return list(top_5_crops)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    features = [N, P, K, temperature, humidity, ph, rainfall]
    
    recommendations = get_crop_recommendations(features, model, scaler, encoder)
    
    return render_template('index.html', recommendations=recommendations)

@app.route('/ideal_environment', methods=['POST'])
def ideal_environment():
    crop_name = request.form['crop_name']
    result = get_ideal_surroundings(crop_name, df)
    
    if result is None:
        return render_template('ideal_environment.html', error=f"Crop {crop_name} not found in the dataset.")
    
    return render_template('ideal_environment.html', result=result, crop_name=crop_name)

if __name__ == "__main__":
    app.run(debug=True)
