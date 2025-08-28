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

Fill in later

- **[01_Exploratory Data Analysis](01_EDA_complete.pdf)** 
- **[02_Preprocessing & Feature Engineering](02_feature_engineering.ipynb)** 
- **[03_Modeling](03_modeling.ipynb)** 
- **[04_Evaluation](04_evaluation.ipynb)** 

## Notebook Descriptions

### 1. [01_Exploratory Data Analysis](01_EDA_complete.pdf)

This notebook conducts systematic exploratory data analysis on NBA play-by-play data spanning 2015-2023, implementing rigorous academic methodology to understand player workload patterns, injury indicators, and data quality for machine learning pipeline development. The analysis covers 4.78 million play-by-play records across 10,460 games and 2,678 unique players from the modern analytics era of professional basketball.

**Key Analytical Findings:**
- **Modern Analytics Era Focus**: Established 2015+ timeframe capturing load management revolution, tracking camera implementation, and post-Warriors championship pace changes, providing 4.78M records across 9 seasons with consistent methodology
- **Player Activity Patterns**: Identified high-usage players led by Giannis Antetokounmpo (30,862 total actions across 661 games), establishing minimum thresholds for modeling candidates (100+ games, substantial action volume) ensuring sufficient data for reliable injury prediction
- **Event Type Distribution**: Analyzed 12 distinct event types with rebounds (22.49%), missed shots (20.22%), and made shots (17.20%) dominating player actions, providing comprehensive workload categorization for physical contact, shooting volume, and defensive activity metrics
- **Data Quality Assessment**: Achieved 98.1% player ID completeness (4.78M of 4.88M records) with robust JOIN performance (31 seconds for 320K records), confirming scalable architecture for feature engineering and real-time prediction pipelines

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
- **Query Performance Optimization**: Verified JOIN operation efficiency with complex multi-table queries processing adequately for large-scale feature engineering, demonstrating production-ready infrastructure for real-time prediction systems
- **Geographic and Demographic Integration**: Player metadata includes physical attributes (height, weight), career span data, draft information, and position classifications enabling risk profiling based on age, size, experience, and role-specific factors

**ML Pipeline Implications:**
- The analysis establishes preprocessing requirements including player filtering strategies (minimum game thresholds), temporal window definitions for rolling metrics, and event classification systems for workload quantification. Injury prediction modeling must incorporate absence pattern recognition, performance decline detection, and position-specific risk factors to achieve reliable performance on this complex, temporally-structured sports dataset.

### 2. [02_Preprocessing & Feature Engineering](02_feature_engineering.ipynb)

This notebook implements comprehensive data preprocessing and feature engineering on NBA play-by-play data, transforming raw game events into sophisticated workload and injury risk indicators. The pipeline creates 76 engineered features across six distinct categories, implementing temporal rolling windows, performance decline detection, and fatigue accumulation metrics while maintaining strict temporal validation to prevent data leakage.

**Key Feature Engineering Categories:**

**Rolling Workload Metrics (3 temporal windows)**
- **Shooting Load Features**: 7-day, 14-day, and 30-day rolling averages combining made shots, missed shots, and free throws (37.4% of player actions), capturing sustained offensive usage patterns
- **Defensive Load Tracking**: Rolling rebound activity across multiple time windows (22.5% of actions), quantifying physical contact and positioning demands
- **Contact Load Assessment**: Combined fouls and free throws over rolling periods (18.7% of actions), measuring physical confrontation intensity and injury risk exposure
- **Ball Handling Stress**: Turnover frequency analysis across temporal windows identifying pressure situations and decision-making workload

**Usage Rate and Intensity Analysis**
- **Actions Per Game Intensity**: Player-relative metrics comparing current activity to historical baselines, normalizing for individual usage patterns (ranges 0.59-1.11x personal averages)
- **Position-Specific Usage Rates**: Shooting, defensive, and contact usage proportions accounting for role-based activity allocation and tactical responsibilities
- **Ball Security Indicators**: Inverse turnover rates measuring ball-handling efficiency under pressure (0.94-1.00 for elite players like Karl-Anthony Towns)
- **Substitution Pattern Analysis**: Frequency metrics serving as fatigue and performance decline indicators

**Performance Comparison Features**
- **Historical Baseline Comparisons**: Season and career averages using expanding windows with shift(1) operations preventing data leakage, transforming absolute statistics into relative performance metrics
- **Anomaly Detection Results**: Identified 242 games exceeding 150% of season average (high-load risk) and 155 games below 50% (potential injury/rest scenarios)
- **Temporal Progression Tracking**: Current game performance ratios against evolving historical patterns, enabling detection when players operate outside typical workload ranges

**Performance Decline Indicators**
- **Multi-Scale Trend Analysis**: 7-day vs 30-day performance comparisons capturing both acute fatigue and chronic performance deterioration patterns
- **Consecutive Pattern Detection**: Sequential low-performance game tracking with 70% personal average threshold, identifying sustained decline periods
- **Efficiency Trend Slopes**: Linear regression slopes over 7-game windows for both volume and efficiency metrics, detecting gradual performance degradation

**Fatigue and Recovery Assessment**
- **Rest Pattern Integration**: Back-to-back game indicators, rest day calculations, and dense scheduling detection (4+ games in 6 days) capturing recovery opportunity variations
- **Seasonal Progression Metrics**: Days and games into season providing cumulative fatigue baselines normalized by 82-game schedule expectations
- **Composite Fatigue Scoring**: Weighted combination (30% recent density, 30% rest deficit, 40% seasonal progression) generating normalized 0-1 fatigue risk indicators

**Contextual Risk Profiling**
- **Physical Attributes Integration**: Age calculation, BMI computation, and position-based risk multipliers (Centers: 1.3x, Point Guards: 0.8x) incorporating biomechanical research
- **Career Experience Factors**: Season experience, lottery pick status, and career span variables capturing veteran wear vs rookie resilience patterns
- **Temporal Context Features**: Season phase indicators, holiday period flags, and playoff push detection accounting for external scheduling pressures

**Data Quality and Preprocessing Achievements:**
- **Temporal Validation Framework**: Implemented expanding window calculations with proper shift operations ensuring no future information leakage, maintaining prediction validity for real-world deployment
- **Missing Value Strategy**: Strategic imputation for first games (neutral 1.0 ratios) and biographical data gaps, achieving complete feature coverage across modeling variables
- **Feature Selection Optimization**: Reduced 76 engineered features to 34 selected variables through correlation analysis and importance ranking, addressing multicollinearity (0.86-0.96 correlations between time windows)
- **Class Imbalance Preparation**: SMOTE balancing on training data maintaining temporal splits, achieving 6,975 training samples with proper 2.4% injury rate representation

**Injury Target Variable Development:**
- **Gap-Based Classification System**: Normal gaps (1-6 days, 94.6%), load management (7-13 days, 2.9%), and injury periods (14+ days, 2.5%) using scheduling analysis methodology
- **Forward-Looking Predictions**: Binary targets for 7-day and 14-day injury risk windows enabling proactive intervention strategies aligned with medical staff decision timelines
- **Population Validation**: Identified injury-prone players (Joel Embiid: 3.4% rate, Anthony Davis: 3.3%) and healthy baselines (Julius Randle: 1.4%, Nikola Jokic: 1.7%) confirming realistic injury distribution patterns

**Temporal Pattern Recognition:**
- **Seasonal Injury Progression**: Demonstrated injury rate escalation from 1.0% (early season) to 8.9% (late season), capturing cumulative fatigue effects and playoff intensity
- **Fatigue Correlation Validation**: Strong relationship between composite fatigue scores and injury occurrence (1.2% at very low fatigue, 6.6% at very high fatigue)
- **Monthly Risk Patterns**: Peak injury periods during April (13.4%), May (14.7%), and August (18.7%) aligned with season-ending intensity and off-season preparation demands

**ML Pipeline Production Readiness:**
- **Dataset Partitioning Strategy**: Created temporally-aware training (6,975 samples), validation (2,567 samples), and test (589 samples) splits preventing data leakage while maintaining representative injury distributions
- **Feature Documentation Framework**: Generated comprehensive feature reference documentation, selection results, and preprocessing configurations enabling model interpretability and deployment consistency
- **Class Weighting Optimization**: Computed balanced class weights (Class 0: 0.51, Class 1: 20.88) addressing severe class imbalance for improved model training performance
- **Serialization and Persistence**: Complete preprocessing pipeline saved with selected features, class weights, and transformation parameters enabling seamless model deployment and real-time inference capabilities

### 3. [03_Modeling](03_modeling.ipynb)

Fill in later

### 4. [04_Evaluation](04_evaluation.ipynb)

Fill in later

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