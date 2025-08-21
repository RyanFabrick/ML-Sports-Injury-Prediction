import json
import boto3
import subprocess
import sys
import os
from datetime import datetime

def install_packages():
    """
    Installs required packages at runtime
    """
    packages = [
        'pandas==1.5.3',
        'numpy==1.24.3', 
        'scikit-learn==1.2.2',
        'xgboost==1.7.5'
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, 
                "--target", "/tmp", "--quiet"
            ])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            raise
    
    # Adds /tmp to Python path so we can import the packages
    if '/tmp' not in sys.path:
        sys.path.insert(0, '/tmp')

def lambda_handler(event, context):
    try:
        print("Starting NBA Injury Prediction Lambda...")
        
        # Tries to import packages, install if missing
        try:
            import pandas as pd
            import numpy as np
            from sklearn.preprocessing import RobustScaler
            import xgboost as xgb
            import pickle
            print("All packages already available")
        except ImportError as e:
            print(f"Missing packages detected: {e}")
            print("Installing packages at runtime...")
            install_packages()
            
            # Import after installation
            import pandas as pd
            import numpy as np
            from sklearn.preprocessing import RobustScaler
            import xgboost as xgb
            import pickle
            print("Packages installed and imported successfully")
        
        # Initializes S3 client
        s3 = boto3.client('s3')
        bucket_name = 'ryan-ml-sports-injury-prediction'
        
        print("Downloading model files from S3...")
        
        # Downloads model files to /tmp directory
        try:
            s3.download_file(bucket_name, 'models/xgboost_20250820_161828.pkl', '/tmp/model.pkl')
            s3.download_file(bucket_name, 'models/nba_injury_predictor_v1_scaler.pkl', '/tmp/scaler.pkl')
            s3.download_file(bucket_name, 'models/selected_features.pkl', '/tmp/features.pkl')
            print("Model files downloaded successfully")
        except Exception as e:
            print(f"Failed to download model files: {e}")
            raise
        
        # Loads the models
        print("Loading models...")
        with open('/tmp/model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        with open('/tmp/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
            
        with open('/tmp/features.pkl', 'rb') as f:
            selected_features = pickle.load(f)
        
        print(f"Models loaded. Using {len(selected_features)} features.")
        
        # Creates sample player data for predictions
        players = [
            {"player_name": "LeBron James", "position": "SF"},
            {"player_name": "Stephen Curry", "position": "PG"}, 
            {"player_name": "Kevin Durant", "position": "PF"},
            {"player_name": "Giannis Antetokounmpo", "position": "PF"},
            {"player_name": "Luka Doncic", "position": "PG"}
        ]
        
        print("Generating sample feature data...")
        # Generate sample data (replace with real player stats later)
        np.random.seed(42)
        sample_data = np.random.uniform(0.1, 1.0, (len(players), len(selected_features)))
        sample_df = pd.DataFrame(sample_data, columns=selected_features)
        
        # Scales the features
        print("Scaling features...")
        sample_scaled = scaler.transform(sample_df)
        
        # Makes predictions
        print("Making injury predictions...")
        predictions = model.predict(sample_scaled)
        probabilities = model.predict_proba(sample_scaled)[:, 1]
        
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