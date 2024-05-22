# Flask Crop Recommendation System

## Overview
This is a Flask-based web application for crop recommendation. It provides suggestions for the best crops to plant based on various input parameters such as soil type, weather conditions, and more.

## Features
- User-friendly web interface
- Real-time crop recommendation
- Historical data analysis
- Integration with various data sources for accurate predictions

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps
1. Clone the repository and navigate to the `flask_app` directory:
    ```sh
    git clone https://github.com/btwitssayan/crop-reco-system.git
    cd crop-reco-system
    git checkout flask-app
    cd flask_app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```sh
    python app.py
    ```

The Flask app will be running at `http://127.0.0.1:5000`.

## Usage
- Open your web browser and go to `http://127.0.0.1:5000`.
- Enter the required input parameters and get crop recommendations.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
