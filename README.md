# Crop Recommendation System

Welcome to the Crop Recommendation System repository. This project contains two separate applications for recommending crops based on various input parameters. The applications are built using two different frameworks: Flask and Streamlit. Each application is maintained in its own branch within this repository.

## Overview

The Crop Recommendation System aims to assist farmers and agricultural professionals in making informed decisions about crop selection based on factors such as soil type, climate conditions, and historical data. By leveraging machine learning algorithms and data analytics techniques, the system provides personalized crop recommendations tailored to specific agricultural environments.

## Features

### Flask Application

- User-friendly web interface for inputting parameters and receiving crop recommendations.
- Real-time prediction of optimal crops based on soil characteristics, weather patterns, and other factors.
- Historical data analysis to identify trends and patterns in crop performance over time.
- Integration with external data sources for enhanced accuracy and reliability.

### Streamlit Application

- Interactive and intuitive web interface for exploring crop recommendations and visualizing data.
- Dynamic visualization of crop performance metrics, including yield, growth patterns, and profitability.
- Customizable input parameters to accommodate various agricultural scenarios and geographic regions.
- Seamless integration with machine learning models for predictive analytics and decision support.

## Documentation

Detailed documentation for each application can be found in their respective branches:

- **Flask Application**: [flask-app/README.md](flask-app/README.md)
- **Streamlit Application**: [streamlit-app/README.md](streamlit-app/README.md)

## References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Purpose

The Crop Recommendation System aims to address the challenges faced by farmers and agricultural stakeholders in selecting the most suitable crops for their specific environmental conditions. By leveraging advanced technologies and data-driven insights, the system empowers users to optimize agricultural productivity, maximize resource utilization, and mitigate risks associated with crop cultivation.

## Conclusion

The Crop Recommendation System represents a valuable tool for enhancing agricultural decision-making and improving farm management practices. By harnessing the power of data analytics and machine learning, the system provides actionable recommendations that enable farmers to achieve sustainable crop production, increase profitability, and contribute to global food security.

## Getting Started

### Setting Up the Repository

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/crop-reco-system.git
    cd crop-reco-system
    ```

### Flask Application Setup

1. **Switch to the `flask-app` branch:**
    ```sh
    git checkout flask-app
    ```

2. **Navigate to the Flask app directory:**
    ```sh
    cd flask_app
    ```

3. **Create a virtual environment and activate it:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Flask application:**
    ```sh
    python app.py
    ```

    The Flask app will be running at `http://127.0.0.1:5000`.

For more detailed information, refer to the `README.md` file in the `flask-app` branch.

### Streamlit Application Setup

1. **Switch to the `streamlit-app` branch:**
    ```sh
    git checkout streamlit-app
    ```

2. **Navigate to the Streamlit app directory:**
    ```sh
    cd streamlit_app
    ```

3. **Create a virtual environment and activate it:**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Streamlit application:**
    ```sh
    streamlit run app.py
    ```

    The Streamlit app will be running at `http://localhost:8501`.

For more detailed information, refer to the `README.md` file in the `streamlit-app` branch.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
