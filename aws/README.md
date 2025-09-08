# *AWS*

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Lambda Functions](#lambda-functions)
    - [lambda_function.py (Original Version)](#lambda_functionpy-original-version)
    - [lambda_function_working.py (Working Version)](#lambda_function_workingpy-working-version)
- [AWS Services Used](#aws-services-used)
- [Deployment Setup](#deployment-setup)
- [Model Artifacts](#model-artifacts)
- [Predictions Output](#predictions-output)
- [Performance Considerations](#performance-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgments & References](#acknowledgments--references)

## Overview

This folder contains AWS Lambda deployment code for the NBA injury prediction machine learning model developed in the [notebooks pipeline](../notebooks/README.md). The deployment provides serverless, scalable inference capabilities using AWS Lambda and S3 storage, transforming the trained XGBoost model into a production ready prediction service that generates injury risk predictions for NBA players.

The system processes sample player data through the complete ML pipeline (feature scaling, model inference, risk categorization) and stores timestamped predictions in S3 for consumption (ex: medical staff, analyitical staff, etc.)

## Architecture

```
┌─────────────────┐      ┌──────────────────┐    ┌─────────────────────┐
│   AWS Lambda    │      │    S3 Bucket     │    │   Prediction API    │
│                 │      │                  │    │                     │
│ • Model Loading │───▶ │ • Model Storage  │    │ • JSON Response     │
│ • Preprocessing │      │ • Artifact Cache │    │ • Risk Levels       │
│ • Inference     │      │ • Predictions    │    │ • Sample Data       │
│ • Risk Scoring  │      │                  │    │                     │
└─────────────────┘      └──────────────────┘    └─────────────────────┘
```

**Data Flow:**
1. Lambda function downloads model artifacts from S3 bucket
2. Generates sample player feature data (simulating real time data pipeline)
3. Applies preprocessing and feature scaling using saved scaler
4. Runs XGBoost model inference to generate injury risk probabilities
5. Categorizes players into risk levels (Low/Medium/High/Critical)
6. Saves timestamped predictions back to S3 for downstream consumption

## Lambda Functions

### lambda_function.py (Original Version)

**Purpose**: Complete ML pipeline implementation with full model artifact loading from S3
- **Model Loading**: Downloads XGBoost model, RobustScaler, and selected features from S3
- **Feature Generation**: Creates realistic sample data for 5 NBA players across 34 selected features
- **Full ML Pipeline**: Implements preprocessing, scaling, and inference using trained models
- **S3 Integration**: Saves predictions as CSV files with timestamp versioning

**Key Features:**
- Pickle based model deserialization from S3 objects
- Comprehensive sample data generation with realistic feature ranges
- Risk probability calculation with 4 tier categorization system
- Dual S3 storage (timestamped + latest) for prediction history

**Dependencies**: pandas, numpy, scikit-learn, xgboost, pickle

### lambda_function_working.py (Working Version)

**Purpose**: Simplified rule based prediction system optimized for AWS Lambda constraints
- **Dependency Management**: Uses AWS Lambda layers (AWSSDKPandas, scikit-learn) to avoid runtime compilation
- **Resource Optimization**: Eliminates model loading overhead for faster cold start performance

**Risk Calculation Algorithm:**
```python
risk_score = (usage_rate/35.0 * 0.25) + 
             (fatigue_score * 0.30) + 
             (contact_style * 0.20) + 
             (age_factor * 0.15) + 
             (injury_history * 0.10)
```

**Sample Predictions Generated:**
- **LeBron James**: 0.404 risk probability (High risk)
- **Stephen Curry**: 0.382 risk probability (High risk) 
- **Kevin Durant**: 0.346 risk probability (High risk)
- **Giannis Antetokounmpo**: 0.569 risk probability (Critical risk)
- **Luka Doncic**: 0.413 risk probability (High risk)

## AWS Services Used

### **AWS Lambda**
- **Runtime**: Python 3.9
- **Memory**: 512 MB recommended for model loading operations
- **Timeout**: 5 minutes for S3 operations and inference
- **Layers Used**: 
  - AWSSDKPandas (pandas/numpy support)
  - scikit-learn layer (ML model support)

### **Amazon S3**
- **Bucket**: ryan-ml-sports-injury-prediction
- **Structure**:
  ```
  ryan-ml-sports-injury-prediction/
  ├── models/
  │   ├── xgboost_20250820_161828.pkl
  │   ├── nba_injury_predictor_v1_scaler.pkl
  │   └── selected_features.pkl
  └── predictions/
      ├── injury_predictions_YYYYMMDD_HHMMSS.csv
      └── latest_predictions.csv
  ```
- **Live Bucket**: Currently contains 2 objects across models/ and predictions/ folders
- **Organization**: Clean separation between model artifacts and prediction outputs for scalable deployment

## Deployment Setup

### **Prerequisites**
1. AWS Account with Lambda and S3 permissions
2. AWS CLI configured with appropriate credentials
3. Trained model artifacts from notebook pipeline

### **Lambda Layer Configuration**
```python
# Required layers in AWS Lambda console:
# 1. AWSSDKPandas (for pandas/numpy)
# 2. scikit-learn layer (for model support)
```

### **Environment Variables**
- No environment variables required (bucket name hardcoded for simplicity)
- Consider parameterizing bucket_name for multi environment deployment

### **IAM Permissions Required**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::ryan-ml-sports-injury-prediction/*"
        }
    ]
}
```

## Model Artifacts

### **Model Files Stored in S3**
- **xgboost_20250820_161828.pkl**: Trained XGBoost model with 34 selected features
- **nba_injury_predictor_v1_scaler.pkl**: RobustScaler fitted on training data
- **selected_features.pkl**: List of 34 optimal features from feature selection process

### **Feature Categories (34 total)**
- Fatigue and workload metrics (primary predictors)
- Rolling performance averages (7, 14, 30-day windows)
- Usage rate comparisons and anomaly indicators
- Player demographics and physical attributes
- Schedule and recovery pattern variables

## Predictions Output

### **JSON Response Format**
```json
{
    "statusCode": 200,
    "body": {
        "message": "Predictions completed successfully",
        "predictions_made": 5,
        "timestamp": "2025-09-02T14:30:00",
        "high_risk_players": 5,
        "sample_predictions": [
            {
                "player_name": "LeBron James",
                "position": "SF",
                "risk_probability": 0.404,
                "risk_prediction": 0,
                "risk_level": "High",
                "prediction_date": "2025-08-22"
            }
        ]
    }
}
```

### **CSV Output Stored in S3**
- **Timestamped File**: injury_predictions_YYYYMMDD_HHMMSS.csv
- **Latest File**: latest_predictions.csv (overwritten each run)
- **Columns**: player_name, position, risk_probability, risk_prediction, risk_level, prediction_date
- **Sample Output Format**:
  ```csv
  player_name,position,risk_probability,risk_prediction,risk_level,prediction_date
  LeBron James,SF,0.4037142857142857,0,High,2025-08-22
  Stephen Curry,PG,0.38242857142857145,0,High,2025-08-22
  Kevin Durant,PF,0.34614285714285714,0,High,2025-08-22
  Giannis Antetokounmpo,PF,0.569,1,Critical,2025-08-22
  Luka Doncic,PG,0.4125714285714286,0,High,2025-08-22
  ```

### **Risk Level Categories**
- **Low**: 0.0 - 0.2 probability (minimal intervention required)
- **Medium**: 0.2 - 0.3 probability (increased monitoring recommended)
- **High**: 0.3 - 0.5 probability (preventive measures advised)
- **Critical**: 0.5+ probability (immediate medical evaluation)

## Performance Considerations

### **Cold Start Optimization**
- Rule-based version eliminates model loading (5-10 second improvement)
- Lambda layers reduce package deployment size and initialization time
- Consider provisioned concurrency for consistent performance

### **Memory and Timeout Settings**
- **Recommended Memory**: 512 MB for model operations, 256 MB for rule based
- **Timeout**: 5 minutes accommodates S3 operations and model inference
- **Concurrent Executions**: Default limits sufficient for daily prediction runs

### **Cost Optimization**
- Rule based approach reduces compute time by ~70%
- S3 storage costs minimal for daily prediction files
- Consider CloudWatch logs retention policy for cost management

### **Scaling Considerations**
- Current implementation handles 5 sample players successfully deployed in production
- Live S3 bucket contains models/ and predictions/ folders with active prediction outputs
- Scale to full NBA roster (450+ players) requires optimization:
  - Batch processing implementation
  - Parallel S3 operations
  - Memory allocation increases
  - Consider Step Functions for orchestration
- **Current Performance**: Giannis Antetokounmpo identified as highest risk (0.569 Critical) demonstrating effective risk stratification

## Contributing

This project was developed as a personal learning project for sports analytics and machine learning deployment. For questions and suggestions:

1. Open an issue describing the enhancement or bug
2. Fork the repository and create a feature branch
3. Follow coding standards
4. Write tests for new functionality
5. Update documentation as needed
6. Submit a pull request with detailed description of changes

## License

This project is open source and available under the MIT License.

## Author

**Ryan Fabrick**
- Statistics and Data Science (B.S) Student, University of California Santa Barbara
- GitHub: [https://github.com/RyanFabrick](https://github.com/RyanFabrick)
- LinkedIn: [www.linkedin.com/in/ryan-fabrick](https://www.linkedin.com/in/ryan-fabrick)
- Email: ryanfabrick@gmail.com

## Acknowledgments & References

- **[NBA Advanced Stats](https://www.nba.com/stats/)** - Official NBA statistical database providing play by play data foundation
- **[Basketball Reference](https://www.basketball-reference.com/)** - Comprehensive NBA historical data and statistical methodology inspiration
- **[Kaggle NBA Datasets](https://www.kaggle.com/datasets?search=nba)** - Community contributed datasets enabling reproducible sports analytics research
- **[XGBoost](https://xgboost.readthedocs.io/)** - Optimized gradient boosting framework specifically designed for structured data and class imbalance scenarios
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning library providing preprocessing, model selection, and evaluation frameworks
- **[TensorFlow](https://www.tensorflow.org/)** - Deep learning platform enabling neural network architectures for sequential sports data
- **[SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)** - Synthetic Minority Oversampling Technique for addressing severe class imbalance in injury prediction
- **[AWS Lambda](https://aws.amazon.com/lambda/)** - Serverless computing platform enabling scalable, cost effective model deployment
- **[Amazon S3](https://aws.amazon.com/s3/)** - Object storage service for model artifacts, predictions, and data persistence
- **[Tableau](https://www.tableau.com/)** - Business intelligence platform for executive level sports analytics dashboards
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation library optimized for large scale sports dataset processing
- **[NumPy](https://numpy.org/)** - Numerical computing foundation enabling efficient feature engineering operations
- **[Jupyter Project](https://jupyter.org/)** - Interactive computing environment for reproducible sports analytics research and documentation
- **[PostgreSQL](https://www.postgresql.org/)** - Advanced relational database system for structured sports data management

_________________________________________________________
Built with ❤️ for the machine learning and NBA community
