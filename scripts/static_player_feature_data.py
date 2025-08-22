import numpy as np
import pandas as pd
from datetime import datetime

def get_realistic_player_features():
    """
    Generate realistic static feature values for NBA players based on their known characteristics
    Based on 2024-25 season patterns and player archetypes
    """
    
    players_data = {
        "LeBron James": {
            # Basic activity metrics - high usage veteran
            "total_actions": 85.2,  # High involvement but age-managed
            "made_shots": 9.8,      # Efficient scorer
            "missed_shots": 12.1,   # High volume shooter
            "free_throws": 4.2,     # Gets to line frequently
            "rebounds": 7.8,        # Strong rebounder
            "fouls": 1.8,           # Disciplined veteran
            "turnovers": 3.8,       # High usage leads to TOs
            "total_shot_attempts": 21.9,
            "shooting_efficiency": 0.448,  # Solid efficiency
            
            # 30-day rolling metrics
            "total_actions_30d": 2556.0,   # 30 games * 85.2
            "shooting_load_30d": 657.0,    # 30 games * 21.9
            "defensive_load_30d": 234.0,   # 30 games * 7.8 rebounds
            "substitution_rate_30d": 0.15,  # Plays heavy minutes
            
            # Usage and contact
            "contact_usage_rate": 0.72,     # Physical player
            "substitution_frequency": 2.1,  # Few subs due to high minutes
            
            # Performance vs season averages
            "shots_vs_season_avg": 1.05,    # Slightly above average
            "rebounds_vs_season_avg": 1.12, # Above average rebounding
            "performance_drop_7vs30": 0.02, # Minimal drop (well-conditioned)
            "current_vs_14day_avg": 0.98,   # Consistent
            "shooting_eff_decline": -0.01,  # Slight decline with age
            "is_low_performance": 0,        # Rarely has bad games
            "consecutive_low_games": 0,
            
            # Trends
            "actions_trend_7d": 0.01,       # Slight upward trend
            "efficiency_trend_7d": -0.005,  # Slight efficiency decline
            
            # Rest and fatigue
            "rest_days_since_last": 1.2,    # Limited rest
            "games_last_14_days": 12,       # Heavy schedule
            "is_back_to_back": 0,           # Rests on back-to-backs now
            "cumulative_actions_30d": 2556.0,
            "fatigue_score": 0.68,          # High fatigue due to age/usage
            
            # Physical attributes
            "bmi": 27.5,                    # Muscular build
            "age_at_game": 39.8,            # Current age
            
            # Schedule context
            "game_day_of_week": 3,          # Wednesday (mid-week)
            "is_weekend_game": 0,
            "is_christmas_period": 0
        },
        
        "Stephen Curry": {
            # Basic activity metrics - elite shooter, lower contact
            "total_actions": 78.5,
            "made_shots": 10.1,      # High shooting volume
            "missed_shots": 12.8,
            "free_throws": 3.9,      # Gets fouled on 3s
            "rebounds": 5.1,         # Lower due to position
            "fouls": 2.2,            # More aggressive on defense now
            "turnovers": 3.2,        # Good ball control
            "total_shot_attempts": 22.9,
            "shooting_efficiency": 0.441,
            
            # 30-day rolling metrics
            "total_actions_30d": 2355.0,
            "shooting_load_30d": 687.0,
            "defensive_load_30d": 153.0,
            "substitution_rate_30d": 0.18,
            
            # Usage and contact
            "contact_usage_rate": 0.45,     # Low contact style
            "substitution_frequency": 2.8,
            
            # Performance vs season averages
            "shots_vs_season_avg": 1.15,    # Well above average shooting
            "rebounds_vs_season_avg": 0.88, # Below average for rebounds
            "performance_drop_7vs30": 0.05, # Some variability
            "current_vs_14day_avg": 1.02,
            "shooting_eff_decline": 0.01,   # Still improving
            "is_low_performance": 0,
            "consecutive_low_games": 0,
            
            # Trends
            "actions_trend_7d": 0.02,
            "efficiency_trend_7d": 0.01,
            
            # Rest and fatigue
            "rest_days_since_last": 1.4,
            "games_last_14_days": 11,
            "is_back_to_back": 0,
            "cumulative_actions_30d": 2355.0,
            "fatigue_score": 0.52,          # Lower fatigue, good conditioning
            
            # Physical attributes
            "bmi": 23.8,                    # Lean build
            "age_at_game": 36.2,
            
            # Schedule context
            "game_day_of_week": 5,          # Friday
            "is_weekend_game": 1,
            "is_christmas_period": 0
        },
        
        "Kevin Durant": {
            # Basic activity metrics - elite scorer, injury concerns
            "total_actions": 82.1,
            "made_shots": 11.2,      # Elite scoring
            "missed_shots": 10.5,    # Efficient shooter
            "free_throws": 5.8,      # Gets to line often
            "rebounds": 6.6,         # Decent for position
            "fouls": 2.1,
            "turnovers": 3.5,
            "total_shot_attempts": 21.7,
            "shooting_efficiency": 0.516,   # Very efficient
            
            # 30-day rolling metrics
            "total_actions_30d": 2463.0,
            "shooting_load_30d": 651.0,
            "defensive_load_30d": 198.0,
            "substitution_rate_30d": 0.16,
            
            # Usage and contact
            "contact_usage_rate": 0.58,     # Moderate contact
            "substitution_frequency": 2.4,
            
            # Performance vs season averages
            "shots_vs_season_avg": 1.08,
            "rebounds_vs_season_avg": 0.95,
            "performance_drop_7vs30": 0.08, # Some inconsistency due to injuries
            "current_vs_14day_avg": 0.95,   # Recent slight decline
            "shooting_eff_decline": 0.02,
            "is_low_performance": 0,
            "consecutive_low_games": 1,     # Occasional off games
            
            # Trends
            "actions_trend_7d": -0.01,      # Slight decline
            "efficiency_trend_7d": 0.005,
            
            # Rest and fatigue
            "rest_days_since_last": 1.8,    # More rest due to injury history
            "games_last_14_days": 10,       # Load management
            "is_back_to_back": 0,
            "cumulative_actions_30d": 2463.0,
            "fatigue_score": 0.61,          # Moderate fatigue
            
            # Physical attributes
            "bmi": 26.1,                    # Tall and lean
            "age_at_game": 36.5,
            
            # Schedule context
            "game_day_of_week": 2,          # Tuesday
            "is_weekend_game": 0,
            "is_christmas_period": 0
        },
        
        "Giannis Antetokounmpo": {
            # Basic activity metrics - high contact, dominant
            "total_actions": 92.8,   # Highest usage
            "made_shots": 11.8,
            "missed_shots": 11.2,
            "free_throws": 7.2,      # Gets fouled frequently
            "rebounds": 11.2,        # Elite rebounder
            "fouls": 3.1,            # Aggressive style
            "turnovers": 4.2,        # High usage leads to TOs
            "total_shot_attempts": 23.0,
            "shooting_efficiency": 0.513,
            
            # 30-day rolling metrics
            "total_actions_30d": 2784.0,    # Highest load
            "shooting_load_30d": 690.0,
            "defensive_load_30d": 336.0,    # High rebounding
            "substitution_rate_30d": 0.12,  # Plays heavy minutes
            
            # Usage and contact
            "contact_usage_rate": 0.85,     # Highest contact rate
            "substitution_frequency": 1.8,  # Rarely sits
            
            # Performance vs season averages
            "shots_vs_season_avg": 1.12,
            "rebounds_vs_season_avg": 1.25, # Well above average
            "performance_drop_7vs30": 0.03, # Very consistent
            "current_vs_14day_avg": 1.01,
            "shooting_eff_decline": -0.005,
            "is_low_performance": 0,
            "consecutive_low_games": 0,
            
            # Trends
            "actions_trend_7d": 0.015,
            "efficiency_trend_7d": 0.008,
            
            # Rest and fatigue
            "rest_days_since_last": 1.1,    # Minimal rest
            "games_last_14_days": 13,       # Heavy workload
            "is_back_to_back": 0,
            "cumulative_actions_30d": 2784.0,
            "fatigue_score": 0.73,          # High fatigue from physical style
            
            # Physical attributes
            "bmi": 28.2,                    # Very muscular
            "age_at_game": 29.8,            # Prime age
            
            # Schedule context
            "game_day_of_week": 6,          # Saturday
            "is_weekend_game": 1,
            "is_christmas_period": 0
        },
        
        "Luka Doncic": {
            # Basic activity metrics - high usage, triple-double threat
            "total_actions": 89.5,
            "made_shots": 9.8,
            "missed_shots": 13.7,    # High volume, lower efficiency
            "free_throws": 6.1,
            "rebounds": 8.9,         # High for a guard
            "fouls": 2.8,
            "turnovers": 4.6,        # High usage leads to TOs
            "total_shot_attempts": 23.5,
            "shooting_efficiency": 0.417,   # Lower efficiency
            
            # 30-day rolling metrics
            "total_actions_30d": 2685.0,
            "shooting_load_30d": 705.0,     # Highest shooting volume
            "defensive_load_30d": 267.0,
            "substitution_rate_30d": 0.14,
            
            # Usage and contact
            "contact_usage_rate": 0.68,
            "substitution_frequency": 2.2,
            
            # Performance vs season averages
            "shots_vs_season_avg": 1.18,    # Well above average
            "rebounds_vs_season_avg": 1.15,
            "performance_drop_7vs30": 0.06, # Some variability
            "current_vs_14day_avg": 0.97,
            "shooting_eff_decline": 0.01,
            "is_low_performance": 0,
            "consecutive_low_games": 1,
            
            # Trends
            "actions_trend_7d": 0.005,
            "efficiency_trend_7d": -0.01,   # Slight decline
            
            # Rest and fatigue
            "rest_days_since_last": 1.3,
            "games_last_14_days": 12,
            "is_back_to_back": 1,           # Playing back-to-back
            "cumulative_actions_30d": 2685.0,
            "fatigue_score": 0.71,          # High fatigue from usage
            
            # Physical attributes
            "bmi": 26.8,                    # Sturdy build
            "age_at_game": 25.9,            # Young prime
            
            # Schedule context
            "game_day_of_week": 1,          # Monday
            "is_weekend_game": 0,
            "is_christmas_period": 1        # Christmas game
        }
    }
    
    return players_data

def create_feature_dataframe():
    """
    Creates a DataFrame with the realistic feature values for all players
    """
    players_data = get_realistic_player_features()
    
    # Defines the feature order to match model
    feature_columns = [
        'total_actions', 'made_shots', 'missed_shots', 'free_throws', 'rebounds', 
        'fouls', 'turnovers', 'total_shot_attempts', 'shooting_efficiency', 
        'total_actions_30d', 'shooting_load_30d', 'defensive_load_30d', 
        'substitution_rate_30d', 'contact_usage_rate', 'substitution_frequency', 
        'shots_vs_season_avg', 'rebounds_vs_season_avg', 'performance_drop_7vs30', 
        'current_vs_14day_avg', 'shooting_eff_decline', 'is_low_performance', 
        'consecutive_low_games', 'actions_trend_7d', 'efficiency_trend_7d', 
        'rest_days_since_last', 'games_last_14_days', 'is_back_to_back', 
        'cumulative_actions_30d', 'fatigue_score', 'bmi', 'age_at_game', 
        'game_day_of_week', 'is_weekend_game', 'is_christmas_period'
    ]
    
    # Creates DataFrame
    df_rows = []
    for player_name, features in players_data.items():
        row = [features[col] for col in feature_columns]
        df_rows.append(row)
    
    df = pd.DataFrame(df_rows, columns=feature_columns)
    df.index = list(players_data.keys())
    
    return df

# Generates the data
if __name__ == "__main__":
    feature_df = create_feature_dataframe()
    print("NBA Player Realistic Feature Values:")
    print(feature_df.round(3))
    
    # Show summary statistics
    print("\nFeature Value Ranges:")
    for col in feature_df.columns:
        print(f"{col:25}: {feature_df[col].min():.3f} - {feature_df[col].max():.3f}")
    
    # Export for Lambda function use
    print("\n\nFor Lambda Function Integration:")
    print()
    
    for i, (player, row) in enumerate(feature_df.iterrows()):
        print(f"# {player}")
        feature_array = row.values.tolist()
        print(f"player_{i}_features = {feature_array}")
        print()