# *NBA Injury Prediction System*

A machine learning system that predicts NBA player injury risk using 4.78 million play by play records spanning 2015-2023. Built with advanced feature engineering, XGBoost optimization, and serverless AWS deployment. Prior to production level implementation, systematic analysis was conducted through four documented notebooks: exploratory data analysis, preprocessing and feature engineering, modeling development, and performance evaluation. Multiple algorithms were evaluated including XGBoost, Logistic Regression, Neural Networks (TensorFlow), and Random Forest.

## Table of Contents

- [AWS, Notebook, SQL, Scripts, & Tableau READMEs](#aws-notebook-sql-scripts--tableau-readmes-more-detail--visual-examples)
- [Overview](#overview)
- [Why Did I Build This?](#why-did-i-build-this)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Demo Screenshots](#demo-screenshots)
- [AWS Environment](#aws-environment)
- [Technology Stack](#technology-stack)
  - [Machine Learning & Data Science](#machine-learning--data-science)
  - [Cloud Infrastructure](#cloud-infrastructure)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Notebooks](#notebooks)
- [Methodology & Sports Analytics Foundation](#methodology--sports-analytics-foundation)
- [Overall Model Performances](#overall-model-performances)
- [Key Feature Insights](#key-feature-insights)
- [Use Cases](#use-cases)
- [Risk Level Classification System](#risk-level-classification-system)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgments & References](#acknowledgments--references)

## AWS, Notebook, SQL, Scripts, & Tableau READMEs (More Detail & Visual Examples)

For more **comprehensive**, **specific**, and **thorough** documentation and examples:
- [AWS README](aws/README.md)
- [Notebooks README](notebooks/README.md)
- [SQL README](sql/README.md)
- [Scripts README](scripts/README.md)
- [Tableau README](tableau/README.md)

## Overview

This project implements an end to end machine learning system for predicting NBA player injury risk using advanced sports analytics methodology. The system processes massive play by play datasets, engineers 76 sophisticated features, and deploys optimized models on AWS for real time risk assessment. This repository provides:

- **Machine Learning Models**: XGBoost, Neural Networks, Random Forest, and Logistic Regression with comprehensive evaluation
- **Serverless AWS Deployment**: Lambda functions with S3 integration for scalable inference
- **Interactive Tableau Dashboard**: Professional visualization for risk analysis and player monitoring 

### Key Results (XGBoost Model)
- **ROC-AUC**: 69.0%
- **Top 20% Risk Capture**: 48.1% of actual injuries identified
- **Precision**: 8.5% (in severely imbalanced dataset)
- **AWS Response Time**: <3 seconds for real time predictions

## Why Did I Build This?

Here's why I created this NBA injury prediction project:

As a passionate Lakers fan born and raised in LA and a lifelong sports enthusiast, I've always been fascinated by the intersection of basketball analytics, machine learning, and data science. Growing up watching players deal with injuries that could make or break championship runs, I became deeply interested in whether modern data science could help predict and prevent these career altering events. The NBA's evolution into the analytics era, with load management becoming a critical strategy and teams investing heavily in sports science, presented the perfect opportunity to explore this question through a machine learning project.

From a technical development perspective, this project allowed me to significantly expand my skill set beyond my existing foundation in Python, Flask, pandas, NumPy, and scikit-learn. While I have solid experience with traditional web development using React, HTML, CSS, TypeScript, and Tailwind CSS, I wanted strengthen my skills and knowledge around the full data science + machine learning pipeline and cloud deployment ecosystem. This project became my gateway to mastering SQL for sports data analysis, implementing serverless AWS architecture with Lambda functions and S3 storage, creating professional business intelligence dashboards in Tableau, and building neural networks with TensorFlow. The combination of my genuine passion for basketball analytics and the opportunity to gain hands on experience with enterprise level technologies made this an ideal project for advancing toward my career goals in software engineering, data science, and machine learning.

The scale and complexity of working with 4.78 million NBA play by play records spanning 2015-2023 also provided invaluable experience in handling real world data challenges from severe class imbalance (only 2.4% injury rate) to temporal validation complexities that prevent data leakage. This project demonstrates not just technical proficiency across the modern data stack, but also the kind of end to end thinking and problem solving approach that's essential for roles in data engineering, machine learning engineering, and applied AI research. It's a good showcase of how I can combine domain expertise, technical skills, and business acumen to deliver production ready solutions that could genuinely impact how professional sports teams approach player health management.

## Key Features

### Analytics Pipeline
- **76 Engineered Features** across fatigue, workload, performance decline, and contextual dimensions
- **Temporal Validation** preventing data leakage with proper time series methodology
- **Class Imbalance Handling** using SMOTE balancing and optimal threshold selection
- **Multi Model Ensemble** with hyperparameter optimization

### Production Deployment
- **Serverless AWS Architecture** with Lambda functions and S3 storage
- **Real time Inference** generating risk predictions for active NBA players
- **Model Versioning** with complete artifact persistence and rollback capability

### Interactive Visualization
- **Player Risk Profiling** showing individual and positional injury patterns
- **Historical Pattern Recognition** identifying seasonal and contextual risk factors

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Data Processing Layer                        │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ play by play│ │ Player Bio  │ │ Game        │                 │
│ │ Events      │ │ Data        │ │ Metadata    │                 │
│ │ (4.78M)     │ │ (2,678)     │ │ (10,460)    │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
└─────────────────────────┼───────────────────────────────────────┘
                          │ 
┌─────────────────────────┼───────────────────────────────────────┐
│               Feature Engineering Pipeline                      │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ Rolling     │ │ Performance │ │ Fatigue     │                 │
│ │ Workload    │ │ Decline     │ │ Composite   │                 │
│ │ (7,14,30d)  │ │ Detection   │ │ Scoring     │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
│                                                                 │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ Usage Rate  │ │ Contextual  │ │ Injury Gap  │                 │
│ │ Anomalies   │ │ Risk        │ │ Analysis    │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
└─────────────────────────┼───────────────────────────────────────┘
                          │ 
┌─────────────────────────┼───────────────────────────────────────┐
│                  Machine Learning Layer                         │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ XGBoost     │ │ Random      │ │ Neural      │                 │
│ │ (Primary)   │ │ Forest      │ │ Network     │                 │
│ │ 69% AUC     │ │ 64.7% AUC   │ │ 59% AUC     │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
│                                                                 │
│ ┌─────────────┐ ┌─────────────┐                                 │
│ │ Logistic    │ │ Feature     │                                 │
│ │ Regression  │ │ Selection   │                                 │
│ │ 64.5% AUC   │ │ (76→34)     │                                 │
│ └─────────────┘ └─────────────┘                                 │
└─────────────────────────┼───────────────────────────────────────┘
                          │ 
┌─────────────────────────┼───────────────────────────────────────┐
│                 Production Deployment                           │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ AWS Lambda  │ │ S3 Storage  │ │ Tableau     │                 │
│ │ Inference   │ │ Models &    │ │ Dashboard   │                 │
│ │ (<3s)       │ │ Predictions │ │             │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

## Demo Screenshots

*There aren't any screenshots of the model itself. Those can be found in the [Notebooks pipeline](notebooks/README.md) with documentation, evlauation, and visualizations. The only demo screenshot here is the Tableau dashboard which has more in depth information in the [Tableau README](tableau/README.md).*

<div align="center">
<img width="645" height="855" alt="tableau screenshot" src="https://github.com/user-attachments/assets/ae6d4e14-3825-4ae3-a9d6-6d321dd2df0c" />
</div>

## AWS Environment
```
┌─────────────────────────────────────────────────────────────────┐
│                     AWS Lambda Function                         │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ Model       │ │ Feature     │ │ Risk        │                 │
│ │ Loading     │ │ Processing  │ │ Scoring     │                 │
│ │ (S3)        │ │ Pipeline    │ │ & Output    │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
└─────────────────────────┼───────────────────────────────────────┘
                          │ 
┌─────────────────────────┼───────────────────────────────────────┐
│                    S3 Storage Buckets                           │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │
│ │ Model       │ │ Scaler &    │ │ Prediction  │                 │
│ │ Artifacts   │ │ Features    │ │ Outputs     │                 │
│ │ (.pkl)      │ │ (.pkl)      │ │ (.csv)      │                 │
│ └─────────────┘ └─────────────┘ └─────────────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

### AWS Lambda Response - Live Predictions
```json
{
  "statusCode": 200,
  "body": {
    "message": "Predictions completed successfully",
    "predictions_made": 5,
    "high_risk_players": 5,
    "sample_predictions": [
      {
        "player_name": "Giannis Antetokounmpo",
        "risk_probability": 0.569,
        "risk_level": "Critical"
      }
    ]
  }
}
```

## Technology Stack

### Machine Learning & Data Science
- **Python**: Primary language for data science pipeline and model development
- **XGBoost**: Gradient boosting framework optimized for structured data and class imbalance
- **Random Forest**: Ensemble method for feature importance analysis and risk stratification
- **Logistic Regression**: Baseline model providing maximum interpretability for real-time alerts
- **Neural Networks (TensorFlow)**: Deep learning architecture for sequential sports data patterns
- **scikit-learn**: ML library for preprocessing, modeling, and evaluation
- **Pandas**: Advanced data manipulation for 4.78M record processing
- **NumPy**: Numerical computing foundation for feature engineering
- **Matplotlib/Seaborn**: Statistical visualization for EDA and model interpretation
- **SMOTE**: Synthetic minority oversampling for class imbalance correction
- **Tableau**: Professional dashboard development for executive reporting

### Cloud Infrastructure  
- **AWS Lambda**: Serverless computing for scalable model inference
- **Amazon S3**: Object storage for model artifacts and prediction outputs
- **AWS SageMaker**: Machine learning platform for model training and deployment
- **PostgreSQL**: Relational database for structured sports data storage
- **SQLite**: Local database for development and feature engineering

## Project Structure

```
ML SPORTS PREDICTION/
├── aws/
│   ├── lambda_function_working.py
│   ├── lambda_function.py
│   └── README.md
├── data/
│   ├── features/
│   ├── processed/
│   └── raw/
├── models/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_evaluation.ipynb
│   └── README.md
├── scripts/
│   ├── dataset_validation.py
│   ├── player_stats_explorer.py
│   ├── static_player_feature_data.py
│   └── README.md
├── sql/
│   ├── EDA.sql
│   ├── feature_engineering.sql
│   └── README.md
├── tableau/
│   ├── NBA Risk Prediction Dashboard.twbx
│   └── README.md
├── venv/
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Quick Start

### Prerequisites
- Python 3.9+
- AWS Account (for deployment)
- Tableau Desktop (for dashboard)
- SQLite Browser (optional)

### 1. Clone Repository
```bash
git clone https://github.com/RyanFabrick/nba-injury-prediction
cd nba-injury-prediction
```

### 2. Environment Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

### 3. Explore the ML Pipeline
```bash
# Run complete notebook pipeline
jupyter notebook notebooks/01_EDA.ipynb
# Follow through 02, 03, 04 notebooks for full analysis

# Or explore individual components
python scripts/dataset_validation.py
python scripts/player_stats_explorer.py
```

### 4. AWS Deployment (Optional)
```bash
# Deploy to AWS Lambda
cd aws/
# Follow deployment_guide.md for complete setup
python lambda_function.py  # Test locally first
```

### 5. Dashboard Visualization
```bash
# Open Tableau dashboard
cd tableau/
# Open NBA_Risk_Dashboard.twbx in Tableau Desktop
```

## Notebooks

The complete machine learning pipeline is documented across four notebooks:

1. **[01_Exploratory Data Analysis](notebooks/01_EDA.ipynb)** 
2. **[02_Preprocessing & Feature Engineering](notebooks/02_feature_engineering.ipynb)**
3. **[03_Modeling](notebooks/03_modeling.ipynb)**
4. **[04_Evaluation](notebooks/04_evaluation.ipynb)**

Each notebook is self contained with thorough documentation. Go to the [Notebooks README](notebooks/README.md) for more information.

## Methodology & Sports Analytics Foundation

### Research Approach
Built using modern sports analytics methodology emphasizing:

- **Temporal Validation**: Strict time series splits preventing data leakage
- **Feature Engineering Excellence**: 76 features capturing fatigue, workload, and performance patterns
- **Class Imbalance Mastery**: SMOTE balancing and threshold optimization for 2.4% injury rate

### Feature Categories
- **Rolling Workload Metrics** (24 features): 7, 14, 30-day windows for shooting, defensive, contact loads
- **Performance Comparison Features** (18 features): Current vs historical baselines with anomaly detection  
- **Fatigue and Recovery Assessment** (12 features): Composite scoring with rest patterns and seasonal progression
- **Usage Rate Analysis** (8 features): Position adjusted intensity metrics and substitution patterns
- **Contextual Risk Profiling** (14 features): Physical attributes, career experience, temporal context

### Injury Classification System
**Injury Definition**: Extended absences (14+ consecutive days) distinguished from load management (7-13 days) and normal rest (1-6 days)

- Eliminates subjective injury reporting bias
- Focuses on observable performance impact
- Enables proactive intervention strategies

## Overall Model Performances

| Model | ROC-AUC | Precision | Recall | F1-Score | Top 20% Capture |
|:------|--------:|----------:|-------:|---------:|----------------:|
| **XGBoost** | **69.0%** | **8.5%** | **35.2%** | **13.8%** | **48.1%** |
| Random Forest | 64.7% | 23.5% | 16.7% | 19.4% | 40.3% |
| Logistic Regression | 64.5% | 7.5% | 45.5% | 13.0% | 37.7% |
| Neural Network | 59.0% | 4.5% | 50.0% | 8.3% | 33.3% |

### XGBoost Model Specifications
- **Architecture**: Maximum depth 3, learning rate 0.1, 100 estimators
- **Regularization**: L1: 0.5, L2: 2.0 for overfitting prevention  
- **Class Handling**: scale_pos_weight=40.77 for severe imbalance (97:1 test ratio)
- **Cross Validation**: 5 fold stratified with 0.143 PR-AUC optimization

### Performance Validation Framework
- **Risk Capture Excellence**: XGBoost identifies 48.1% of injuries in top 17% predictions
- **Precision Recall Trade off**: Random Forest achieves highest precision (23.5%) for focused screening
- **Temporal Generalization**: Proper time series validation confirms real world applicability
- **Clinical Decision Support**: Risk stratification enables targeted medical intervention

## Key Feature Insights

### Universal Injury Predictors (Across All Models)
1. **Fatigue Score Dominance**: Primary predictor with 8.1-15.4% feature importance
2. **Performance Decline Indicators**: Current vs 14-day average consistently ranks top 5
3. **Day of Week Scheduling**: Contextual risk variation (4.8-6.6% importance)
4. **Defensive Load Accumulation**: Physical contact frequency over rolling windows
5. **Usage Rate Anomalies**: Statistical deviations from personal baselines

### Position Specific Risk Patterns
- **Centers**: 1.3x baseline injury risk (high contact, size factors)
- **Point Guards**: 0.8x baseline risk (lower contact, higher conditioning)
- **Power Forwards**: 1.2x baseline risk (paint activity, rebounding stress)
- **Shooting Guards/Small Forwards**: 1.0x baseline (balanced risk profile)

### Seasonal Injury Progression
- **Early Season** (Oct-Dec): 1.0% injury rate (conditioning phase)
- **Mid Season** (Jan-Mar): 2.5% injury rate (cumulative fatigue)
- **Late Season** (Apr-May): 8.9% injury rate (playoff intensity)
- **Off-Season** (Jun-Aug): 18.7% injury rate (training/preparation)

### Counterintuitive Findings
- **Back to Back Games**: Protective association (-1.467 coefficient) suggesting load management selection bias
- **High Usage Players**: Lower relative injury risk due to superior conditioning and medical support
- **Veteran Experience**: Mixed results. Experience might reduce some risks but age increases others

## Use Cases

### For NBA Teams & Medical Staff
- **Proactive Load Management**: 7-14 day prediction windows enable preventive rest scheduling
- **Resource Allocation**: Focus medical attention on statistically high risk players  
- **Performance Optimization**: Balance competitive demands with injury prevention
- **Contract Negotiations**: Risk assessment for player valuations and insurance

### For Players & Agents
- **Career Longevity**: Understand personal risk factors for extended playing careers
- **Training Optimization**: Identify workload thresholds and recovery requirements
- **Contract Strategy**: Leverage injury risk data in negotiations and team selection
- **Performance Planning**: Seasonal periodization based on injury risk patterns

### For Sports Analytics & Research
- **Methodology Validation**: Temporal validation framework for sports prediction models
- **Feature Engineering Innovation**: Advanced techniques for sequential sports data
- **Class Imbalance Solutions**: Approaches for rare event prediction in sports
- **Production Deployment**: MLOps best practices for sports analytics applications

### For Fantasy Sports & Betting
- **Player Availability**: Predict lineup changes and rest game probabilities
- **Performance Forecasting**: Incorporate injury risk into statistical projections
- **Market Inefficiencies**: Identify undervalued players with low injury risk profiles
- **Risk Management**: Portfolio construction considering injury correlation patterns

## Risk Level Classification System
```python
# Production risk thresholds
if risk_probability >= 0.5:
    return "Critical"    # Immediate medical evaluation
elif risk_probability >= 0.3:
    return "High"        # Preventive measures advised  
elif risk_probability >= 0.2:
    return "Medium"      # Increased monitoring
else:
    return "Low"         # Minimal intervention
```

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
- **[Kaggle NBA Datasets](https://www.kaggle.com/datasets/wyattowalsh/basketball)** - Public kaggle dataset enabling reproducible sports analytics research from creator Wyatt Walsh
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

This personal project demonstrates my machine learning engineering capabilities, cloud infrastructure skills, and data analytics specialization. As a UCSB Statistics and Data Science student with a genuine passion for basketball, data science and engineering, and software engineering, I designed this as an end to end showcase of my technical abilities across the complete ML pipeline. From EDA on massive datasets (4.78M records) and feature engineering (76 features) to AWS serverless deployment and professional Tableau dashboards. It highlights my skills in implementing and optimizing diverse ML algorithms including XGBoost, Random Forest, TensorFlow Neural Networks, and Logistic Regression, handling severe class imbalance, temporal validation methodologies, MLOps with AWS Lambda and S3, business and data visualization, and my overall ability to bridge the gap between technical complexity and real world applications.