import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

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
        return f"Crop {crop_name} not found in the dataset."
    
    ideal_surroundings = crop_data.mean()
    return ideal_surroundings

def get_crop_recommendations(features, model, scaler, label_encoder):
    # Scale the input features
    features_scaled = scaler.transform([features])
    
    # Predict probabilities
    probabilities = model.predict_proba(features_scaled)[0]
    
    # Get the top 5 crop recommendations
    top_5_indices = np.argsort(probabilities)[-5:][::-1]
    top_5_crops = label_encoder.inverse_transform(top_5_indices)
    
    return list(top_5_crops)

def main():
    st.title("Crop Recommendation System")

    st.sidebar.title("Choose an option")
    option = st.sidebar.selectbox("", ["Get crop recommendations", "Get ideal environment for a crop", "Exit"])

    if option == "Get crop recommendations":
        st.header("Enter the features for crop recommendation:")
        N = st.number_input("Nitrogen (N)", min_value=0.0, format="%.2f")
        P = st.number_input("Phosphorus (P)", min_value=0.0, format="%.2f")
        K = st.number_input("Potassium (K)", min_value=0.0, format="%.2f")
        temperature = st.number_input("Temperature", min_value=0.0, format="%.2f")
        humidity = st.number_input("Humidity", min_value=0.0, format="%.2f")
        pH = st.number_input("pH", min_value=0.0, format="%.2f")
        rainfall = st.number_input("Rainfall", min_value=0.0, format="%.2f")

        features = [N, P, K, temperature, humidity, pH, rainfall]

        if st.button("Get Recommendations"):
            top_5_crops = get_crop_recommendations(features, model, scaler, encoder)
            st.write("Top 5 crop recommendations:")
            for crop in top_5_crops:
                st.write(f"{crop}")

    elif option == "Get ideal environment for a crop":
        crop_name = st.text_input("Enter the crop name:")

        if st.button("Get Ideal Environment"):
            result = get_ideal_surroundings(crop_name, df)
            if isinstance(result, str):
                st.write(result)
            else:
                st.write(f"For growing {crop_name}:")
                st.write(f"Nitrogen: {round(result['N'])}")
                st.write(f"Phosphorus: {round(result['P'])}")
                st.write(f"Potassium: {round(result['K'])}")
                st.write(f"Temperature: {round(result['temperature'])}")
                st.write(f"Humidity: {round(result['humidity'])}")
                st.write(f"pH Level: {round(result['ph'])}")
                st.write(f"Rainfall: {round(result['rainfall'])}")

    elif option == "Exit":
        st.write("Goodbye!")

if __name__ == "__main__":
    main()
