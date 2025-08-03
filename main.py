import pickle 
import pandas as pd
import numpy as np
import logging
import os
from flask import Flask, request, render_template

# Create Flask app
app = Flask(__name__)

# # Configure logging for Google Cloud
# if os.environ.get('GAE_ENV', '').startswith('standard'):
#     # Production on App Engine
#     import google.cloud.logging
#     client = google.cloud.logging.Client()
#     client.setup_logging()
# else:
#     # Local development
#     logging.basicConfig(level=logging.INFO)

# Load model (with error handling)
model = pickle.load(open('pipe.pkl','rb'))
# model = None
# try:
#     if os.path.exists('pipe.pkl'):
#         model = pickle.load(open('pipe.pkl','rb'))
#         app.logger.info("Model loaded successfully")
#     else:
#         app.logger.error("Model file 'pipe.pkl' not found")
# except Exception as e:
#     app.logger.error(f"Error loading model: {e}")

# @app.before_request
# def log_request_info():
#     app.logger.info('Request: %s %s', request.method, request.url)

@app.route("/")
def home():
    try:
        return render_template('form.html')
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return render_template('form.html', 
                                        prediction_text="Error: Model not loaded. Please check server logs.")
        
        # Get form data
        square_feet = request.form.get('squareFeet')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        year_built = request.form.get('yearBuilt')
        neighborhood = request.form.get('area')
        
        # Validate all fields are present
        if not all([square_feet, bedrooms, bathrooms, year_built, neighborhood]):
            return render_template('form.html', 
                                        prediction_text="Error: Please fill in all fields.")
        
        # Convert to appropriate types
        try:
            square_feet = float(square_feet)
            bedrooms = int(bedrooms)
            bathrooms = float(bathrooms)
            year_built = int(year_built)
        except ValueError:
            return render_template('form.html', 
                                        prediction_text="Error: Please enter valid numbers.")
        
        # Create input dataframe
        input_data = pd.DataFrame([{
            'SquareFeet': square_feet,
            'Bedrooms': bedrooms,
            'Bathrooms': bathrooms,
            'YearBuilt': year_built,
            'Neighborhood': neighborhood
        }])
        
        # Make prediction
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)
        
        return render_template('form.html', 
                                    prediction_text=f"Predicted House Price: ${output:,.2f}")
        
    except Exception as e:
        app.logger.error(f"Prediction error: {e}")
        return render_template('form.html', 
                                    prediction_text=f"Error making prediction: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)