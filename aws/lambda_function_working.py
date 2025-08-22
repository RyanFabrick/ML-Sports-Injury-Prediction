import json
import boto3
import subprocess
import sys
import os
from datetime import datetime

# IMPORTANT: commented out bc I added AWSSDKPands layer in AWS console to prevent runtime compling errors.
# IMPORTANT also added second layer got scikitlearn
# def install_packages():
#     """
#     Installs required packages at runtime
#     """
#     packages = [
#         'pandas==1.5.3',
#         'numpy==1.24.3', 
#         'scikit-learn==1.2.2',
#         'xgboost==1.7.5'
#     ]
    
#     for package in packages:
#         print(f"Installing {package}...")
#         try:
#             subprocess.check_call([
#                 sys.executable, "-m", "pip", "install", package, 
#                 "--target", "/tmp", "--quiet"
#             ])
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to install {package}: {e}")
#             raise
    
#     # Adds /tmp to Python path so we can import the packages
#     if '/tmp' not in sys.path:
#         sys.path.insert(0, '/tmp')

def lambda_handler(event, context):
    try:
        print("Starting NBA Injury Prediction Lambda...")
        
        # Tries to import packages, install if missing
        try:
            import pandas as pd
            import numpy as np
            # from sklearn.preprocessing import RobustScaler
            # import xgboost as xgb
            import pickle
            print("All packages already available")
        except ImportError as e:
            print(f"Missing packages detected: {e}")
            print("Installing packages at runtime...")
            #install_packages()
            
            # Import after installation
            import pandas as pd
            import numpy as np
            # from sklearn.preprocessing import RobustScaler
            # import xgboost as xgb
            import pickle
            print("Packages installed and imported successfully")
        
        # Initializes S3 client
        s3 = boto3.client('s3')
        bucket_name = 'ryan-ml-sports-injury-prediction'
        
        # print("Downloading model files from S3...")
        
        # Downloads model files to /tmp directory
        # try:
        #     s3.download_file(bucket_name, 'models/xgboost_20250820_161828.pkl', '/tmp/model.pkl')
        #     s3.download_file(bucket_name, 'models/nba_injury_predictor_v1_scaler.pkl', '/tmp/scaler.pkl')
        #     s3.download_file(bucket_name, 'models/selected_features.pkl', '/tmp/features.pkl')
        #     print("Model files downloaded successfully")
        # except Exception as e:
        #     print(f"Failed to download model files: {e}")
        #     raise
        
        # Loads the models
        # print("Loading models...")
        # with open('/tmp/model.pkl', 'rb') as f:
        #     model = pickle.load(f)
        
        # with open('/tmp/scaler.pkl', 'rb') as f:
        #     scaler = pickle.load(f)
            
        # with open('/tmp/features.pkl', 'rb') as f:
        #     selected_features = pickle.load(f)
        
        # print(f"Models loaded. Using {len(selected_features)} features.")
        
        # Creates sample player data for predictions
        players = [
            {"player_name": "LeBron James", "position": "SF"},
            {"player_name": "Stephen Curry", "position": "PG"}, 
            {"player_name": "Kevin Durant", "position": "PF"},
            {"player_name": "Giannis Antetokounmpo", "position": "PF"},
            {"player_name": "Luka Doncic", "position": "PG"}
        ]
        
        print("Generating sample feature data...")
        # Generates sample data (via static features player script)
        np.random.seed(42)
        sample_data = np.array([
            [85.2, 9.8, 12.1, 4.2, 7.8, 1.8, 3.8, 21.9, 0.448, 2556.0, 657.0, 234.0, 0.15, 0.72, 2.1, 1.05, 1.12, 0.02, 0.98, -0.01, 0.0, 0.0, 0.01, -0.005, 1.2, 12.0, 0.0, 2556.0, 0.68, 27.5, 39.8, 3.0, 0.0, 0.0],  # LeBron James
            [78.5, 10.1, 12.8, 3.9, 5.1, 2.2, 3.2, 22.9, 0.441, 2355.0, 687.0, 153.0, 0.18, 0.45, 2.8, 1.15, 0.88, 0.05, 1.02, 0.01, 0.0, 0.0, 0.02, 0.01, 1.4, 11.0, 0.0, 2355.0, 0.52, 23.8, 36.2, 5.0, 1.0, 0.0],  # Stephen Curry
            [82.1, 11.2, 10.5, 5.8, 6.6, 2.1, 3.5, 21.7, 0.516, 2463.0, 651.0, 198.0, 0.16, 0.58, 2.4, 1.08, 0.95, 0.08, 0.95, 0.02, 0.0, 1.0, -0.01, 0.005, 1.8, 10.0, 0.0, 2463.0, 0.61, 26.1, 36.5, 2.0, 0.0, 0.0],  # Kevin Durant
            [92.8, 11.8, 11.2, 7.2, 11.2, 3.1, 4.2, 23.0, 0.513, 2784.0, 690.0, 336.0, 0.12, 0.85, 1.8, 1.12, 1.25, 0.03, 1.01, -0.005, 0.0, 0.0, 0.015, 0.008, 1.1, 13.0, 0.0, 2784.0, 0.73, 28.2, 29.8, 6.0, 1.0, 0.0],  # Giannis Antetokounmpo
            [89.5, 9.8, 13.7, 6.1, 8.9, 2.8, 4.6, 23.5, 0.417, 2685.0, 705.0, 267.0, 0.14, 0.68, 2.2, 1.18, 1.15, 0.06, 0.97, 0.01, 0.0, 1.0, 0.005, -0.01, 1.3, 12.0, 1.0, 2685.0, 0.71, 26.8, 25.9, 1.0, 0.0, 1.0]   # Luka Doncic
        ])
        # sample_df = pd.DataFrame(sample_data, columns=selected_features)
        
        # Scales the features
        # print("Scaling features...")
        # sample_scaled = scaler.transform(sample_df)
        
        # Makes predictions
        # print("Making injury predictions...")
        # predictions = model.predict(sample_scaled)
        # probabilities = model.predict_proba(sample_scaled)[:, 1]
        
        # REPLACEMENT: Rule based prediction system using realistic data
        def calculate_injury_risk(player_features):
            """Calculate injury risk based on key factors"""
            
            # Key risk factor indices (based on feature structure)
            usage_rate = player_features[4] if len(player_features) > 4 else 20.0  # Usage Rate
            fatigue_score = player_features[28] if len(player_features) > 28 else 0.5  # Fatigue Score
            contact_style = player_features[13] if len(player_features) > 13 else 0.5  # Contact Style
            age = player_features[31] if len(player_features) > 31 else 28.0  # Age
            injury_history = player_features[32] if len(player_features) > 32 else 0.0  # Previous injuries
            
            # Calculate composite risk score
            risk_score = 0.0
            
            # Usage rate factor (normalize high usage as risky)
            usage_factor = min(usage_rate / 35.0, 1.0)
            risk_score += usage_factor * 0.25
            
            # Fatigue factor
            risk_score += fatigue_score * 0.30
            
            # Contact style factor  
            risk_score += contact_style * 0.20
            
            # Age factor (players over 30 have increased risk)
            age_factor = max(0, (age - 25) / 15.0)  # Scale 25-40 to 0-1
            risk_score += age_factor * 0.15
            
            # Injury history
            risk_score += injury_history * 0.10
            
            # Ensure score is between 0.1 and 0.9
            risk_score = max(0.1, min(0.9, risk_score))
            
            return risk_score
        
        print("Making injury predictions...")
        
        # Generate predictions for each player using rule-based system
        predictions = []
        probabilities = []
        for i in range(len(players)):
            prob = calculate_injury_risk(sample_data[i])
            pred = 1 if prob >= 0.5 else 0
            predictions.append(pred)
            probabilities.append(prob)
            print(f"{players[i]['player_name']}: Risk = {prob:.3f}")
        
        # Creates results with risk levels
        results = []
        for i, player in enumerate(players):
            prob = probabilities[i]
            pred = predictions[i]
            
            # Determine risk level
            if prob >= 0.5:
                risk_level = "Critical"
            elif prob >= 0.3:
                risk_level = "High"
            elif prob >= 0.2:
                risk_level = "Medium"
            else:
                risk_level = "Low"
            
            results.append({
                "player_name": player["player_name"],
                "position": player["position"],
                "risk_probability": float(prob),
                "risk_prediction": int(pred),
                "risk_level": risk_level,
                "prediction_date": datetime.now().strftime("%Y-%m-%d")
            })
        
        print("Saving results to S3...")
        
        # Converts to DataFrame and save as CSV
        results_df = pd.DataFrame(results)
        csv_content = results_df.to_csv(index=False)
        
        # Generates timestamp for file naming
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Saves timestamped file
        s3.put_object(
            Bucket=bucket_name,
            Key=f'predictions/injury_predictions_{timestamp}.csv',
            Body=csv_content,
            ContentType='text/csv'
        )
        
        # Saves latest predictions file
        s3.put_object(
            Bucket=bucket_name,
            Key='predictions/latest_predictions.csv',
            Body=csv_content,
            ContentType='text/csv'
        )
        
        high_risk_count = sum(1 for r in results if r['risk_prediction'] == 1)
        
        print(f"Predictions completed. {high_risk_count} high-risk players identified.")
        
        # Returns success response
        response_body = {
            "message": "Predictions completed successfully",
            "predictions_made": len(results),
            "timestamp": datetime.now().isoformat(),
            "high_risk_players": high_risk_count,
            "sample_predictions": results
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
        
    except Exception as e:
        error_msg = f"Lambda function error: {str(e)}"
        print(error_msg)
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": str(e),
                "message": "Prediction failed"
            })
        }