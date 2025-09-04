import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
import zipfile
import tempfile
import os

def validate_basketball_dataset(db_path, is_zip=False):
    """
    Quick validation script for the Wyatt Walsh basketball dataset
    """
    
    print("NBA Dataset Validation Report")
    
    # Handles zip file if needed (I extracted it manually)
    if is_zip:
        with zipfile.ZipFile(db_path, 'r') as zip_ref:
            # Find the .sqlite file in the zip
            sqlite_files = [f for f in zip_ref.namelist() if f.endswith('.sqlite')]
            if not sqlite_files:
                print("No .sqlite file found in zip!")
                return
            
            # Extracts to temp location
            with tempfile.TemporaryDirectory() as temp_dir:
                zip_ref.extract(sqlite_files[0], temp_dir)
                temp_db_path = os.path.join(temp_dir, sqlite_files[0])
                conn = sqlite3.connect(temp_db_path)
    else:
        # Connects directly to SQLite database
        conn = sqlite3.connect(db_path)
    
    # 1. Checks for the available tables
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(tables_query, conn)
    print(f"\nAvailable Tables ({len(tables)}):")
    for table in tables['name']:
        print(f"  - {table}")
    
    # 2. Checks key tables for injury prediction (updated for actual table names)
    key_tables = ['game', 'other_stats', 'player', 'team']
    
    for table in key_tables:
        if table in tables['name'].values:
            print(f"\n{table.upper()} TABLE:")
            
            # Gets the table structure
            columns_query = f"PRAGMA table_info({table});"
            columns = pd.read_sql_query(columns_query, conn)
            print(f"   Columns: {list(columns['name'])}")
            
            # Gets the sample data
            sample_query = f"SELECT * FROM {table} LIMIT 3;"
            sample = pd.read_sql_query(sample_query, conn)
            print(f"   Rows: {len(pd.read_sql_query(f'SELECT COUNT(*) as count FROM {table}', conn))} records")
            print(f"   Sample: {list(sample.columns)[:8]}...")  # Shows first 8 columns only
            
        else:
            print(f"\n{table.upper()} TABLE: Not found")
    
    # 3. Checks for injury prediction essentials
    print(f"\nINJURY PREDICTION READINESS:")
    
    # Looks for game-level data
    if 'game' in tables['name'].values:
        games_sample = pd.read_sql_query("SELECT * FROM game LIMIT 5", conn)
        print(f"   Game data available: {len(games_sample)} sample records")
        
        # Checks for date columns
        date_columns = [col for col in games_sample.columns if 'date' in col.lower()]
        print(f"   Date columns: {date_columns}")
    
    # Looks for player stats
    if 'other_stats' in tables['name'].values:
        stats_sample = pd.read_sql_query("SELECT * FROM other_stats LIMIT 5", conn)
        print(f"   Player stats available: other_stats")
        
        # Checks for key workload metrics
        workload_cols = [col for col in stats_sample.columns if any(metric in col.lower() 
                        for metric in ['minutes', 'mp', 'min', 'usage', 'touches'])]
        print(f"   Workload metrics: {workload_cols}")
        
    # Checks if play_by_play for detailed game data
    if 'play_by_play' in tables['name'].values:
        pbp_sample = pd.read_sql_query("SELECT * FROM play_by_play LIMIT 3", conn)
        print(f"   Play-by-play data available: {len(pbp_sample)} sample records")
    
    # 4. Time range analysis
    print(f"\nDATA TIMEFRAME:")
    try:
        # Tries different date column possibilities
        date_queries = [
            "SELECT MIN(game_date) as min_date, MAX(game_date) as max_date FROM game",
            "SELECT MIN(date) as min_date, MAX(date) as max_date FROM game",
            "SELECT MIN(game_date_est) as min_date, MAX(game_date_est) as max_date FROM game"
        ]
        
        for query in date_queries:
            try:
                date_range = pd.read_sql_query(query, conn)
                print(f"   Range: {date_range['min_date'].iloc[0]} to {date_range['max_date'].iloc[0]}")
                break
            except:
                continue
    except:
        print("   Could not determine date range - check other columns")
    
    # 5. Data volume assessment
    print(f"\nDATA VOLUME (for ML viability):")
    
    for table in ['game', 'other_stats', 'player']:
        if table in tables['name'].values:
            count_query = f"SELECT COUNT(*) as count FROM {table}"
            count = pd.read_sql_query(count_query, conn)['count'].iloc[0]
            
            # Assesses if sufficient for ML
            if table == 'game' and count >= 5000:
                print(f"   {table}: {count:,} records (sufficient for ML)")
            elif table == 'other_stats' and count >= 50000:
                print(f"   {table}: {count:,} records (excellent for ML)")
            elif table == 'player' and count >= 1000:
                print(f"   {table}: {count:,} records (good coverage)")
            else:
                print(f"   {table}: {count:,} records (check if sufficient)")
    
    print(f"\nPROJECT VIABILITY ASSESSMENT:")
    
    has_games = 'game' in tables['name'].values
    has_stats = 'other_stats' in tables['name'].values
    has_players = 'player' in tables['name'].values
    
    if has_games and has_stats and has_players:
        print("    EXCELLENT: All core tables present - proceed with project...")
        print("      1. Explore 'other_stats' table for player workload features")
        print("      2. Check date formats in 'game' table")
        print("      3. Look for minutes played, usage rate in other_stats")
        print("      4. Consider performance decline as injury proxy")
        print("      5. Use play_by_play data for detailed analysis")
    elif has_games and has_stats:
        print("   GOOD: Core data available - project viable with some limitations")
    else:
        print("   CONCERNING: Missing key tables - may need to find alternative dataset")
    
    conn.close()

if __name__ == "__main__":
    db_path = r"PUT_ACTUAL_PATH_HERE\nba_database.sqlite"  # Update with actual path
    validate_basketball_dataset(db_path)