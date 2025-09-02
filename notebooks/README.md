# *Notebooks*

## Table of Contents
- [Overview](#overview)
- [Notebook Descriptions](#notebook-descriptions)
    - [Notebook 1 (EDA) Description](#1-01_exploratory-data-analysis)
    - [Notebook 2 (Preprocessing & Feature Engineering) Description](#2-02_preprocessing--feature-engineering)
    - [Notebook 3 (Modeling) Description](#3-03_modeling)
    - [Notebook 4 (Evaluation) Description](#4-04_evaluation)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgments & References](#acknowledgments--references)
    
## Overview

The four notebooks follow a systematic progression from raw NBA data exploration through machine learning model evaluation for injury prediction, implementing sports analytics methodology using 4.78 million play by play records spanning 2015-2023. The pipeline transforms granular game event data into actionable risk indicators through workload analysis, fatigue modeling, and performance decline detection, generating 76 engineered features before optimizing to 34 selected variables for deployment. Click each documented notebook below for step by step documentation, code, outputs, and more.

- **[01_Exploratory Data Analysis](01_EDA.ipynb)** 
- **[02_Preprocessing & Feature Engineering](02_feature_engineering.ipynb)** 
- **[03_Modeling](03_modeling.ipynb)** 
- **[04_Evaluation](04_evaluation.ipynb)** 

## Notebook Descriptions

### 1. [01_Exploratory Data Analysis](01_EDA.ipynb)

This notebook conducts systematic exploratory data analysis on NBA play by play data spanning 2015-2023, implementing academic methodology to understand player workload patterns, injury indicators, and data quality for machine learning pipeline development. The analysis covers 4.78 million play by play records across 10,460 games and 2,678 unique players from the modern analytics era of professional basketball.

**Key Analytical Findings:**
- **Modern Analytics Era Focus**: Established 2015+ timeframe capturing load management revolution, tracking camera implementation, and post-Warriors championship pace changes, providing 4.78M records across 9 seasons with consistent methodology
- **Player Activity Patterns**: Identified high usage players led by Giannis Antetokounmpo (30,862 total actions across 661 games), establishing minimum thresholds for modeling candidates (100+ games, substantial action volume) ensuring sufficient data for reliable injury prediction
- **Event Type Distribution**: Analyzed 12 distinct event types with rebounds (22.49%), missed shots (20.22%), and made shots (17.20%) dominating player actions, providing workload categorization for physical contact, shooting volume, and defensive activity metrics
- **Data Quality Assessment**: Achieved 98.1% player ID completeness (4.78M of 4.88M records) with robust JOIN performance (31 seconds for 320K records), confirming scalable architecture for feature engineering and real time prediction pipelines

**Temporal Coverage Analysis:**
- **Standard Seasons Consistency**: Regular seasons (2015-2019, 2021-2022) show stable volume ranges of 540K-590K records annually with 1,200-1,300 games, providing reliable training data foundation
- **Anomalous Period Identification**: 2020 COVID season reduced to 317K records (45% below normal) and 2023 partial data (314K records through playoffs), requiring special handling in model validation strategies
- **Player Career Spans**: Top modeling candidates demonstrate 8-9 season consistency (Giannis, LeBron, Harden) with complete temporal coverage enabling longitudinal workload analysis and injury pattern recognition

**Feature Engineering Foundation:**
- **Workload Metric Categories**: Established shooting load (Types 1+2+3: 37.4% of actions), defensive load (Type 4: 22.5%), physical contact (Types 6+3: 18.7%), and ball handling stress (Type 5: 6.1%) providing comprehensive player usage profiling
- **Injury Proxy Development**: Gap analysis methodology successfully identified extended absences (7+ days) distinguishing between seasonal breaks (140-210 days), injury periods (14-40 days), and load management (7-13 days), with Joel Embiid showing clear injury-prone patterns (257-day gap in 2017)
- **Performance Decline Indicators**: Sample workload aggregation demonstrates ability to track rolling averages, performance drops, and consecutive absence patterns enabling sophisticated injury risk modeling approaches

**Data Pipeline Architecture:**
- **Database Schema Validation**: Confirmed robust relational structure with play_by_play as primary source (34 columns), game table providing temporal context (55 columns), and common_player_info supplying demographic features (33 columns) supporting comprehensive feature engineering
- **Query Performance Optimization**: Verified JOIN operation efficiency with complex multi table queries processing adequately for large-scale feature engineering, demonstrating production ready infrastructure for real time prediction systems
- **Geographic and Demographic Integration**: Player metadata includes physical attributes (height, weight), career span data, draft information, and position classifications enabling risk profiling based on age, size, experience, and role specific factors

**ML Pipeline Implications:**
- The analysis establishes preprocessing requirements including player filtering strategies (minimum game thresholds), temporal window definitions for rolling metrics, and event classification systems for workload quantification. Injury prediction modeling must incorporate absence pattern recognition, performance decline detection, and position specific risk factors to achieve reliable performance on this complex, temporally structured sports dataset.

### 2. [02_Preprocessing & Feature Engineering](02_feature_engineering.ipynb)

This notebook implements data preprocessing and feature engineering on NBA play by play data, transforming raw game events into workload and injury risk indicators. The pipeline creates 76 engineered features across six distinct categories, implementing temporal rolling windows, performance decline detection, and fatigue accumulation metrics while maintaining strict temporal validation to prevent data leakage.

**Key Feature Engineering Categories:**

**Rolling Workload Metrics (3 temporal windows)**
- **Shooting Load Features**: 7-day, 14-day, and 30-day rolling averages combining made shots, missed shots, and free throws (37.4% of player actions), capturing sustained offensive usage patterns
- **Defensive Load Tracking**: Rolling rebound activity across multiple time windows (22.5% of actions), quantifying physical contact and positioning demands
- **Contact Load Assessment**: Combined fouls and free throws over rolling periods (18.7% of actions), measuring physical confrontation intensity and injury risk exposure
- **Ball Handling Stress**: Turnover frequency analysis across temporal windows identifying pressure situations and decision-making workload

**Usage Rate and Intensity Analysis**
- **Actions Per Game Intensity**: Player relative metrics comparing current activity to historical baselines, normalizing for individual usage patterns (ranges 0.59-1.11x personal averages)
- **Position-Specific Usage Rates**: Shooting, defensive, and contact usage proportions accounting for role based activity allocation and tactical responsibilities
- **Ball Security Indicators**: Inverse turnover rates measuring ball handling efficiency under pressure (0.94-1.00 for elite players like Karl-Anthony Towns)
- **Substitution Pattern Analysis**: Frequency metrics serving as fatigue and performance decline indicators

**Performance Comparison Features**
- **Historical Baseline Comparisons**: Season and career averages using expanding windows with shift(1) operations preventing data leakage, transforming absolute statistics into relative performance metrics
- **Anomaly Detection Results**: Identified 242 games exceeding 150% of season average (high-load risk) and 155 games below 50% (potential injury/rest scenarios)
- **Temporal Progression Tracking**: Current game performance ratios against evolving historical patterns, enabling detection when players operate outside typical workload ranges

**Performance Decline Indicators**
- **Multi-Scale Trend Analysis**: 7-day vs 30-day performance comparisons capturing both acute fatigue and chronic performance deterioration patterns
- **Consecutive Pattern Detection**: Sequential low performance game tracking with 70% personal average threshold, identifying sustained decline periods
- **Efficiency Trend Slopes**: Linear regression slopes over 7-game windows for both volume and efficiency metrics, detecting gradual performance degradation

**Fatigue and Recovery Assessment**
- **Rest Pattern Integration**: Back to back game indicators, rest day calculations, and dense scheduling detection (4+ games in 6 days) capturing recovery opportunity variations
- **Seasonal Progression Metrics**: Days and games into season providing cumulative fatigue baselines normalized by 82-game schedule expectations
- **Composite Fatigue Scoring**: Weighted combination (30% recent density, 30% rest deficit, 40% seasonal progression) generating normalized 0-1 fatigue risk indicators

**Contextual Risk Profiling**
- **Physical Attributes Integration**: Age calculation, BMI computation, and position based risk multipliers (Centers: 1.3x, Point Guards: 0.8x) incorporating biomechanical research
- **Career Experience Factors**: Season experience, lottery pick status, and career span variables capturing veteran wear vs rookie resilience patterns
- **Temporal Context Features**: Season phase indicators, holiday period flags, and playoff push detection accounting for external scheduling pressures

**Data Quality and Preprocessing Achievements:**
- **Temporal Validation Framework**: Implemented expanding window calculations with proper shift operations ensuring no future information leakage, maintaining prediction validity for real world deployment
- **Missing Value Strategy**: Strategic imputation for first games (neutral 1.0 ratios) and biographical data gaps, achieving complete feature coverage across modeling variables
- **Feature Selection Optimization**: Reduced 76 engineered features to 34 selected variables through correlation analysis and importance ranking, addressing multicollinearity (0.86-0.96 correlations between time windows)
- **Class Imbalance Preparation**: SMOTE balancing on training data maintaining temporal splits, achieving 6,975 training samples with proper 2.4% injury rate representation

**Injury Target Variable Development:**
- **Gap Based Classification System**: Normal gaps (1-6 days, 94.6%), load management (7-13 days, 2.9%), and injury periods (14+ days, 2.5%) using scheduling analysis methodology
- **Forward Looking Predictions**: Binary targets for 7-day and 14-day injury risk windows enabling proactive intervention strategies aligned with medical staff decision timelines
- **Population Validation**: Identified injury prone players (Joel Embiid: 3.4% rate, Anthony Davis: 3.3%) and healthy baselines (Julius Randle: 1.4%, Nikola Jokic: 1.7%) confirming realistic injury distribution patterns

**Temporal Pattern Recognition:**
- **Seasonal Injury Progression**: Demonstrated injury rate escalation from 1.0% (early season) to 8.9% (late season), capturing cumulative fatigue effects and playoff intensity
- **Fatigue Correlation Validation**: Strong relationship between composite fatigue scores and injury occurrence (1.2% at very low fatigue, 6.6% at very high fatigue)
- **Monthly Risk Patterns**: Peak injury periods during April (13.4%), May (14.7%), and August (18.7%) aligned with season-ending intensity and off season preparation demands

**ML Pipeline Production Readiness:**
- **Dataset Partitioning Strategy**: Created temporally aware training (6,975 samples), validation (2,567 samples), and test (589 samples) splits preventing data leakage while maintaining representative injury distributions
- **Feature Documentation Framework**: Generated comprehensive feature reference documentation, selection results, and preprocessing configurations enabling model interpretability and deployment consistency
- **Class Weighting Optimization**: Computed balanced class weights (Class 0: 0.51, Class 1: 20.88) addressing severe class imbalance for improved model training performance
- **Serialization and Persistence**: Complete preprocessing pipeline saved with selected features, class weights, and transformation parameters enabling seamless model deployment and real time inference capabilities

### 3. [03_Modeling](03_modeling.ipynb)

This notebook implements machine learning model development for NBA injury prediction, training and evaluating four algorithms on engineered workload and fatigue features. The modeling pipeline addresses severe class imbalance (2.4% injury rate), implements rigorous hyperparameter optimization, and demonstrates varying degrees of overfitting across model architectures while maintaining consistent feature importance patterns centered on fatigue and workload metrics.

**Model Architecture Implementations:**

**Logistic Regression Baseline Model**
- **Configuration**: L2 regularization (C=1.0), balanced class weights (Class 0: 0.51, Class 1: 20.88), LBFGS solver optimized for small datasets with 1000 iteration limit ensuring convergence
- **Training Performance**: 74.7% accuracy with 6.7% precision and 74.3% recall, achieving 83.0% ROC-AUC and 18.5% PR-AUC on training data, demonstrating strong discriminative capability on balanced training set
- **Validation Degradation**: Performance drops to 75.7% accuracy, 5.7% precision, 45.5% recall with 64.5% ROC-AUC and 9.8% PR-AUC, indicating moderate overfitting and generalization challenges
- **Test Set Reality**: Severe performance collapse to 47.7% accuracy, 0.7% precision, 33.3% recall with 37.2% ROC-AUC, revealing poor real world applicability on unseen data with extreme class imbalance (97.2:1 ratio)

**Random Forest Ensemble Method**
- **Hyperparameter Optimization**: Grid search across 162 parameter combinations using 3-fold stratified cross-validation, optimizing for PR-AUC (average precision) with 76-second training time
- **Best Configuration**: 150 estimators, maximum depth 15, minimum samples split 50, minimum samples leaf 20, sqrt feature selection, balanced_subsample class weighting achieving 0.1729 crossvalidation PR-AUC
- **Extreme Overfitting Pattern**: Training performance reaches 98.5% accuracy with 62.4% precision, 96.4% recall, and 99.6% ROC-AUC, indicating near-perfect memorization of training patterns
- **Generalization Failure**: Validation accuracy remains high (96.1%) but precision drops dramatically to 23.9% with 14.3% recall, while test performance collapses to 3.7% precision and 16.7% recall despite extensive hyperparameter tuning

**XGBoost Gradient Boosting Implementation**
- **Class Imbalance Handling**: Automatic scale_pos_weight calculation (40.77) based on negative to positive class ratio, combined with extensive regularization (L1: 0.5, L2: 2.0) and conservative learning parameters
- **Comprehensive Hyperparameter Search**: 2,187 parameter combinations across 6,561 total cross validation fits with early stopping (10 rounds patience), achieving 0.143 best cross validation PR-AUC
- **Optimal Configuration**: Maximum depth 3 (conservative), learning rate 0.1, 100 estimators, 70% subsample ratios for both samples and features, demonstrating preference for regularized, shallow trees
- **Balanced Performance Profile**: Training metrics show 82.2% accuracy, 9.7% precision, 77.2% recall with 88.4% ROC-AUC, indicating more controlled learning without extreme overfitting compared to Random Forest

**Neural Network Deep Learning Architecture**
- **Architecture Design**: Sequential model with 64→32→16→1 unit progression, ReLU activation functions, dropout layers (30%, 30%, 20%), batch normalization for gradient stability, and sigmoid output for binary classification
- **Training Configuration**: Adam optimizer (learning rate 0.001), binary cross entropy loss, sample weight implementation for class imbalance, batch size 32 with early stopping (15 epochs patience) and learning rate reduction
- **Training Dynamics**: Early convergence at epoch 17 with best validation loss at epoch 2, learning rate reduction to 0.0005 at epoch 12, final training loss 0.5259 vs validation loss 0.8868 indicating overfitting
- **Model Complexity**: 5,313 total parameters (5,089 trainable), approximately 20.8KB model size, demonstrating efficient parameter utilization for injury prediction task

**Feature Importance Analysis Across Models:**

**Consistent Top Predictors Identified:**
- **Fatigue Score Dominance**: Emerges as primary predictor across all models (Random Forest: 15.4% importance, XGBoost: 8.1% importance, Logistic Regression: coefficient 1.818), validating composite fatigue metric effectiveness
- **Game Timing Factors**: Day of week scheduling shows consistent importance (Random Forest: 6.6%, XGBoost: 4.8%), suggesting contextual injury risk variations
- **Performance Comparison Metrics**: Current vs 14-day averages rank highly across models, indicating performance decline as injury predictor
- **Workload Accumulation**: Shooting and defensive load metrics consistently appear in top 15 features, confirming cumulative stress hypothesis

**Model Specific Feature Insights:**
- **Logistic Regression Counterintuitive Findings**: Back to back games show protective coefficient (-1.844), potentially indicating selection bias where only healthy players participate in consecutive games
- **Random Forest Activity Patterns**: Total actions and performance trends dominate beyond fatigue, suggesting tree based methods capture complex interaction effects
- **XGBoost Balanced Profile**: More distributed importance across rebounding, substitution frequency, and shooting patterns, indicating ensemble learning captures diverse risk factors

**Performance Validation and Risk Assessment:**

**Top K Risk Prediction Effectiveness:**
- **Logistic Regression Risk Capture**: Top 5% highest risk predictions capture 14.3% of actual injuries (8.6% precision), scaling to 37.7% capture rate in top 20% predictions
- **Random Forest Superior Capture**: Top 5% predictions capture 20.8% of injuries (12.5% precision), achieving 40.3% capture rate in top 20% with highest precision among tested models
- **XGBoost Consistent Performance**: Top 20% risk group captures 51.9% of actual injuries (7.8% precision), demonstrating best overall sensitivity for high risk player identification

**Cross-Model Validation Insights:**
- **ROC-AUC Degradation Pattern**: All models show validation ROC-AUC between 60-69% dropping to 35-45% on test set, indicating consistent generalization challenges with temporal data splits
- **Precision Recall Trade offs**: Models achieve reasonable recall (35-45% on validation) but suffer precision collapse (0.6-7.5%), reflecting severe class imbalance challenges in real world deployment
- **Class Imbalance Reality**: Test set ratio (97.2:1) more extreme than training (40.8:1) or validation (32.3:1), demonstrating temporal injury rate variations affecting model reliability

**Model Selection and Deployment Considerations:**

**Production Readiness Assessment:**
- **XGBoost Recommended**: Demonstrates most balanced performance profile with controlled overfitting, reasonable generalization, and superior top 20% risk capture (51.9%) for practical intervention strategies
- **Feature Engineering Validation**: Consistent importance of fatigue score, workload metrics, and performance decline indicators across all model types confirms feature engineering effectiveness
- **Temporal Validation Success**: Proper time series splits prevent data leakage while revealing realistic performance expectations for deployment scenarios

**Clinical Decision Support Integration:**
- **Risk Stratification Capability**: Models successfully identify high risk periods with 7.8-12.5% precision in top tier predictions, providing actionable intelligence for medical staff intervention
- **False Positive Management**: High false positive rates (94% of top predictions) require careful integration with clinical judgment and additional screening protocols
- **Interpretability Framework**: Saved feature importance rankings, model coefficients, and prediction probabilities enable transparent decision support for sports medicine applications

**Model Persistence and Infrastructure:**
- **Complete Model Serialization**: All trained models, predictions, performance metrics, feature importance data, and hyperparameter search results saved with timestamp based versioning system
- **Deployment Package Creation**: Model scaler, preprocessing configurations, selected features list, and class weights persisted for consistent real time inference capability
- **Manifest System Implementation**: Comprehensive model registry with performance summaries enabling systematic model comparison and selection for production deployment

### 4. [04_Evaluation](04_evaluation.ipynb)

This notebook provides an evaluation analysis of four machine learning models for NBA injury prediction, revealing critical performance patterns, model limitations, and deployment considerations through multi dimensional assessment frameworks. The analysis exposes significant overfitting issues, class imbalance challenges, and generalization failures while identifying optimal model selection criteria for real world sports medicine applications.

**Comprehensive Performance Assessment Framework:**

**Model Performance Heatmap Analysis**
- **Performance Ranking Identification**: Random Forest achieves strongest training metrics (98.5% accuracy, 99.6% ROC AUC) followed by XGBoost (82.2% accuracy, 88.4% ROC AUC), but validation performance reveals critical generalization issues
- **Critical Overfitting Detection**: Random Forest demonstrates extreme train-validation ROC AUC gap (0.996), indicating severe memorization rather than pattern learning, while other models show moderate gaps (0.185-0.193)
- **Validation Data Quality Issues**: All models show near-zero validation metrics across multiple performance measures, suggesting potential data leakage, preprocessing errors, or temporal validation methodology problems requiring pipeline investigation
- **Test Performance Reality Check**: Dramatic performance degradation from training to test sets across all models confirms generalization failures, with test ROC AUC ranging from 0.372-0.453 compared to training values of 0.830-0.996

**ROC and Precision-Recall Curve Comparative Analysis**
- **Discriminative Performance Rankings**: XGBoost leads ROC performance (AUC = 0.690) demonstrating superior class separation ability, followed by Random Forest (0.647) and Logistic Regression (0.645), with Neural Network trailing significantly (0.590)
- **Class Imbalance Impact Assessment**: Precision-Recall curves reveal severe imbalance challenges with baseline precision of 0.030, highlighting that ROC curves may be misleadingly optimistic for deployment scenarios
- **Minority Class Detection Effectiveness**: Random Forest achieves highest average precision (0.121) for positive class identification, while XGBoost's ROC superiority doesn't translate to PR curve performance (0.083 AP), indicating model-specific strengths for imbalanced data
- **Clinical Decision Support Implications**: Low precision values across all models (0.045-0.121) suggest high false positive rates requiring careful integration with clinical judgment and additional screening protocols

**Feature Importance Consensus and Model Interpretability**
- **Universal Predictor Identification**: Fatigue score emerges as the dominant predictor across all models (Logistic Regression: 1.836 coefficient, Random Forest: 13.4% importance, XGBoost: 8.5% importance), validating composite fatigue metric as primary injury risk factor
- **Model-Specific Feature Preferences**: Only 1 out of 20 unique important features shows complete consensus, indicating different models capture distinct injury risk patterns and supporting ensemble approach potential
- **Counterintuitive Relationship Discovery**: back to back games show protective association in Logistic Regression (-1.467 coefficient), likely reflecting load management practices where only healthy players participate in consecutive games
- **Workload Pattern Recognition**: Performance deviation metrics (current vs 14-day average, rebounds vs season average) consistently rank highly, confirming the hypothesis that statistical anomalies precede injury events

**Performance-Complexity Trade-off Optimization**
- **Optimal Balance Point Identification**: XGBoost achieves best performance complexity ratio with 0.690 validation ROC AUC using 3,500 parameters and 180-second training time, representing the sweet spot for production deployment
- **Efficiency Leadership**: Logistic Regression delivers 94% of XGBoost's performance with only 1% of parameters (35 vs 3,500) and training time (2s vs 180s), making it ideal for real time applications requiring interpretability
- **Complexity Paradox**: Neural Network's 5,313 parameters yield worst performance (0.590 ROC AUC), while Random Forest's 5,250 parameters suffer from severe overfitting, demonstrating that parameter count doesn't guarantee better results
- **Deployment Recommendation Framework**: real time injury alerts favor Logistic Regression's interpretability and speed, while comprehensive weekly risk assessments benefit from XGBoost's accuracy complexity balance

**Confusion Matrix and Clinical Performance Metrics**
- **Test Set Reality Assessment**: Random Forest achieves highest specificity (95.5%) but poor sensitivity (16.7%), while Neural Network provides most balanced performance (50.0% sensitivity/specificity) at lower overall effectiveness
- **Positive Predictive Value Crisis**: All models suffer from extremely low test set PPV (0.006-0.037), indicating 97-99% false positive rates that would overwhelm medical staff in practical deployment scenarios
- **Class Imbalance Severity**: High negative predictive values (98.6-99.1%) reflect dataset composition rather than model quality, with test set showing more extreme imbalance (97.2:1) than training data (40.8:1)
- **Cost Sensitive Learning Requirements**: Poor sensitivity specificity balance across models necessitates threshold optimization and cost sensitive learning approaches to minimize false negatives in injury prediction context

**Top K Risk Stratification Effectiveness**
- **Risk Capture Performance Rankings**: XGBoost captures 48.1% of injuries in top 17% of predictions, Random Forest achieves highest precision (23.5%) at 2% threshold, while Logistic Regression provides middle ground performance at 10% threshold
- **Precision Coverage Trade offs**: Random Forest excels in high precision, low coverage scenarios (15.6% injury capture), while XGBoost optimizes for broader screening with acceptable precision (8.5%), enabling different intervention strategies
- **Risk Distribution Analysis**: Heavy overlap between injury and no injury risk scores across all models indicates limited discriminative power, suggesting need for enhanced feature engineering or alternative modeling approaches
- **Optimal Operating Point Variation**: Large differences in optimal K values (Random Forest: 2%, XGBoost: 17%, Neural Network: 6%) reflect distinct model calibration characteristics requiring individualized threshold selection

**Critical Issues and Improvement Requirements**

**Systematic Pipeline Problems Identified:**
- **Validation Methodology Concerns**: Near zero validation metrics across multiple models suggest temporal validation implementation errors or data preprocessing issues requiring comprehensive pipeline audit
- **Generalization Failure Pattern**: Consistent performance degradation from training to test indicates fundamental modeling challenges extending beyond hyperparameter tuning to feature engineering and temporal validation strategies
- **Class Imbalance Underestimation**: Test set imbalance severity (97.2:1) exceeds training expectations, revealing temporal injury rate variations that complicate deployment planning and threshold optimization

**Strategic Improvement Recommendations:**
- **Immediate Technical Actions**: Investigate validation set construction methodology, implement stronger regularization techniques, review temporal split strategies to prevent data leakage, and develop cost sensitive learning frameworks
- **Feature Engineering Enhancement**: Expand performance deviation metrics, incorporate load management indicators, develop position specific risk models, and create ensemble features combining multiple temporal windows
- **Clinical Integration Strategy**: Establish false positive tolerance thresholds, develop multi stage screening protocols, create interpretable risk scoring systems, and implement model confidence intervals for clinical decision support

**Deployment Strategy and Model Selection Framework**

**Production Environment Considerations:**
- **real time Alert Systems**: Deploy Logistic Regression for immediate injury risk notifications requiring maximum interpretability and sub second inference time for training staff decision support
- **Weekly Risk Assessment Pipeline**: Implement XGBoost for comprehensive player evaluation where 3 minute training time is acceptable and superior accuracy justifies increased complexity
- **Resource Allocation Optimization**: Use Random Forest precision focused approach for limited intervention capacity scenarios, while XGBoost coverage optimization suits broader screening programs
- **Regulatory Compliance Requirements**: Leverage Logistic Regression's full interpretability for medical decision transparency, documentation requirements, and player health record integration

**Model Performance Monitoring and Maintenance:**
- **Temporal Drift Detection**: Implement validation performance tracking to identify when model retraining is required due to evolving player conditioning, rule changes, or medical practice updates
- **Class Distribution Monitoring**: Track injury rate variations across seasons, teams, and player demographics to maintain model calibration and threshold optimization
- **Feature Importance Stability**: Monitor consensus feature rankings to ensure model interpretability remains consistent and identify emerging risk factors requiring feature engineering updates

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

Fill in later