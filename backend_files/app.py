
# Import necessary libraries
import numpy as np
import joblib  # For loading the serialized model
import pandas as pd  # For data manipulation
from flask import Flask, request, jsonify  # For creating the Flask API
import xgboost as xgb # Import xgboost to load native XGBoost models

# Initialize Flask app with a name
super_subscribe_api = Flask("super_subscribe_api") #code to define the name of the app

# Load the trained churn prediction model
# If the model was saved using best_xgb_model.save_model() as a JSON file
model = xgb.XGBClassifier() # Initialize an XGBClassifier
model.load_model("final_subscription_model.json") # Load the model from the JSON file

# Load the preprocessor (assuming it was saved separately during training)
# IMPORTANT: Ensure 'preprocessor.joblib' exists in the 'backend_files' directory
# This preprocessor should be the one that transforms raw features into the 41 features
# that your 'model' expects.
try:
    preprocessor = joblib.load("preprocessor.joblib")
except FileNotFoundError:
    print("Error: 'preprocessor.joblib' not found. Ensure your preprocessing pipeline is saved and available.")
    # Exit or raise an error in a real deployment scenario
    exit()

# Define a route for the home page
@super_subscribe_api.get('/')
def home():
    return "Welcome to the Subscription Prediction API!" #code to define a welcome message

# Define an endpoint to predict churn for a single customer
@super_subscribe_api.post('/v1/predict')
def predict_subscriptions():
    # Get JSON data from the request
    data = request.get_json()

    # Extract relevant raw customer features from the input data.
    # IMPORTANT: This dictionary MUST contain ALL the raw features that your 'preprocessor'
    # was trained on, and in the correct format (e.g., original categorical values, not one-hot encoded).
    # Any missing features here will cause issues with the preprocessor or model.
    # For illustration, we include the features provided by the frontend:
    sample_raw_features = {
        'Month': data['Month'],
        'Day_of_Week': data['Day_of_Week'],
        'Duration': data['Duration'],
        'housing': data['housing'],
        'job': data['job'],
        'loan': data['loan']
        # Add ALL other raw features expected by your preprocessor here.
        # For example: 'age', 'marital', 'education', 'default', 'balance', 'contact',
        # 'campaign', 'pdays', 'previous', 'poutcome', with appropriate default/placeholder values if not from frontend.
    }

    # Convert the extracted raw data into a DataFrame
    raw_input_df = pd.DataFrame([sample_raw_features])

    # Apply the preprocessor to transform raw input into the format expected by the model
    # This will generate the 41 features that the model was trained on.
    processed_input_data = preprocessor.transform(raw_input_df)

    # Make a churn prediction using the trained model
    prediction = model.predict(processed_input_data).tolist()[0]

    # Return the prediction as a JSON response
    return jsonify({'Subscription': prediction})


# Run the Flask app in debug mode
if __name__ == '__main__':
    super_subscribe_api.run(debug=True)
