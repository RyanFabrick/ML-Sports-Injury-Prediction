import sqlite3
import pandas as pd

def explore_player_level_data(db_path):
    """
    Checks for individual player game statistics in the database
    """
    conn = sqlite3.connect(db_path)
    
    print("Searching for Player-Level Game Stats")

    
    # Checks if play_by_play has player data
    print("\n PLAY_BY_PLAY TABLE:")
    pbp_sample = pd.read_sql_query("SELECT * FROM play_by_play LIMIT 3", conn)
    print(f"Columns: {list(pbp_sample.columns)}")
    
    # Looks for player_id columns
    player_cols = [col for col in pbp_sample.columns if 'player' in col.lower()]
    print(f"Player related columns: {player_cols}")
    
    # Checks common_player_info
    print("\n COMMON_PLAYER_INFO TABLE:")
    player_info = pd.read_sql_query("SELECT * FROM common_player_info LIMIT 3", conn)
    print(f"Columns: {list(player_info.columns)}")
    print(f"Sample data shape: {player_info.shape}")
    
    # Checks if I can derive player stats from play_by_play
    if 'player_id' in pbp_sample.columns or any('player' in col.lower() for col in pbp_sample.columns):
        print("\nPOTENTIAL SOLUTION:")
        print("   Play-by-play contains player data!")
        print("   We can aggregate individual player stats from play-by-play actions")
        print("   This could give us very detailed workload metrics:")
        print("      - Minutes played (time stamps)")
        print("      - Shot attempts (workload)")
        print("      - Defensive actions (physical load)")
        print("      - Substitution patterns (fatigue indicators)")
    
    # Checka for any other tables that might have player game stats
    print("\n CHECKING OTHER TABLES FOR PLAYER STATS:")
    
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(tables_query, conn)
    
    for table_name in tables['name']:
        if table_name not in ['game', 'other_stats', 'player', 'team']:
            try:
                sample = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 1", conn)
                player_related = [col for col in sample.columns if 'player' in col.lower()]
                game_related = [col for col in sample.columns if 'game' in col.lower()]
                
                if player_related and game_related:
                    print(f"   {table_name}: Has both player and game columns!")
                    print(f"      Player cols: {player_related[:3]}...")
                    print(f"      Game cols: {game_related[:3]}...")
                    
                    count = pd.read_sql_query(f"SELECT COUNT(*) as count FROM {table_name}", conn)['count'].iloc[0]
                    print(f"      Records: {count:,}")
                    
            except Exception as e:
                print(f"   {table_name}: Could not analyze - {str(e)[:50]}...")
    
    print("\nRECOMMENDATION:")
    print("   If play_by_play has player_id, this dataset is PERFECT!")
    print("   If not, I need to find a supplementary player stats dataset")
    
    conn.close()

if __name__ == "__main__":
    db_path = r"PUT_ACTUAL_PATH_HERE\nba_database.sqlite"  # Update with actual path
    explore_player_level_data(db_path)