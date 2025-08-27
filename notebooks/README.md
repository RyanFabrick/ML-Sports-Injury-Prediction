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

Fill in later

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