import json
import boto3
import pickle
import pandas as pd
import numpy as np
from io import BytesIO
import logging
from datetime import datetime

# Sets up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda function to make NBA injury predictions
    Downloads model from S3, processes input data, returns predictions
    """
    
    try:
        # Initializes S3 client
        s3_client = boto3.client('s3')
        bucket_name = 'ryan-ml-sports-injury-prediction'
        
        # Downloads model artifacts from S3
        logger.info("Downloading model artifacts from S3...")
        
        # Downloads XGBoost model
        model_obj = s3_client.get_object(Bucket=bucket_name, Key='models/xgboost_20250820_161828.pkl')
        model = pickle.load(BytesIO(model_obj['Body'].read()), encoding='latin1')
        
        # Downloads scaler
        scaler_obj = s3_client.get_object(Bucket=bucket_name, Key='models/nba_injury_predictor_v1_scaler.pkl')
        scaler = pickle.load(BytesIO(scaler_obj['Body'].read()))
        
        # Downloads selected features
        features_obj = s3_client.get_object(Bucket=bucket_name, Key='models/selected_features.pkl')
        selected_features = pickle.load(BytesIO(features_obj['Body'].read()), encoding='latin1')
        
        logger.info(f"Model loaded successfully. Features: {len(selected_features)}")
        
        # Creates sample prediction data (replace with real data in production)
        sample_data = create_sample_data(selected_features)
        
        # Makes predictions
        predictions = make_predictions(model, scaler, sample_data, selected_features)
        
        # Saves predictions to S3
        save_predictions_to_s3(s3_client, bucket_name, predictions)
        
        # Returns response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Predictions completed successfully',
                'predictions_made': len(predictions),
                'timestamp': datetime.now().isoformat(),
                'high_risk_players': int(sum(predictions['risk_probability'] > 0.3)),
                'sample_predictions': predictions.head(5).to_dict('records')
            })
        }
        
    except Exception as e:
        logger.error(f"Error in lambda function: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Prediction failed'
            })
        }

def create_sample_data(selected_features):
    """
    Creates sample data for testing - replace with real data pipeline
    """
    # Sample player data (normalized values similar to training data)
    sample_players = [
        {'player_name': 'LeBron James', 'age': 39, 'position': 'SF'},
        {'player_name': 'Stephen Curry', 'age': 35, 'position': 'PG'},
        {'player_name': 'Kevin Durant', 'age': 35, 'position': 'PF'},
        {'player_name': 'Giannis Antetokounmpo', 'age': 29, 'position': 'PF'},
        {'player_name': 'Luka Doncic', 'age': 25, 'position': 'PG'}
    ]
    
    # Generates realistic feature values
    np.random.seed(42)  # For consistent results
    n_players = len(sample_players)
    n_features = len(selected_features)
    
    # Creates feature matrix with realistic ranges
    data = []
    for i, player in enumerate(sample_players):
        row = {}
        for j, feature in enumerate(selected_features):
            # Generates realistic values based on feature type
            if 'age' in feature.lower():
                row[feature] = player['age'] + np.random.normal(0, 2)
            elif 'minutes' in feature.lower():
                row[feature] = np.random.normal(30, 8)  # Average NBA minutes
            elif 'games' in feature.lower():
                row[feature] = np.random.normal(65, 10)  # Games per season
            elif 'rest' in feature.lower():
                row[feature] = np.random.exponential(2)  # Rest days
            elif 'usage' in feature.lower() or 'rate' in feature.lower():
                row[feature] = np.random.normal(0.25, 0.05)  # Usage rates
            else:
                row[feature] = np.random.normal(0, 1)  # Standardized features
        
        row['player_name'] = player['player_name']
        row['position'] = player['position']
        data.append(row)
    
    return pd.DataFrame(data)

def make_predictions(model, scaler, data, selected_features):
    """
    Makes injury risk predictions
    """
    # Prepares feature matrix
    X = data[selected_features].values
    
    # Scales features
    X_scaled = scaler.transform(X)
    
    # Makes predictions
    risk_probabilities = model.predict_proba(X_scaled)[:, 1]  # Probability of injury
    risk_predictions = (risk_probabilities > 0.2).astype(int)  # Binary prediction
    
    # Creates results dataframe
    results = data[['player_name', 'position']].copy()
    results['risk_probability'] = risk_probabilities
    results['risk_prediction'] = risk_predictions
    results['risk_level'] = pd.cut(risk_probabilities, 
                                   bins=[0, 0.1, 0.3, 0.5, 1.0], 
                                   labels=['Low', 'Medium', 'High', 'Critical'])
    results['prediction_date'] = datetime.now().strftime('%Y-%m-%d')
    
    return results

def save_predictions_to_s3(s3_client, bucket_name, predictions):
    """
    Saves predictions to S3 as CSV
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Converts to CSV
    csv_buffer = BytesIO()
    predictions.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    # Uploads to S3
    key = f'predictions/injury_predictions_{timestamp}.csv'
    s3_client.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=csv_buffer.getvalue(),
        ContentType='text/csv'
    )
    
    # Saves as latest
    s3_client.put_object(
        Bucket=bucket_name,
        Key='predictions/latest_predictions.csv',
        Body=csv_buffer.getvalue(),
        ContentType='text/csv'
    )
    
    logger.info(f"Predictions saved to S3: {key}")

# Tests function for local development
if __name__ == "__main__":
    # Mock event and context for local testing
    test_event = {}
    test_context = {}
    
    result = lambda_handler(test_event, test_context)
    print(json.dumps(result, indent=2))