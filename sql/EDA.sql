-- =============================================================================
-- TABLE INFORMATION & SCHEMA QUERIES
-- =============================================================================

-- Get all table names in database
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name;

-- Get record count for each table
SELECT COUNT(*) as count FROM {table};

-- Get table schema information
PRAGMA table_info({table});

-- Sample data from table
SELECT * FROM {table} LIMIT 3;

-- =============================================================================
-- play by play DATA EXPLORATION
-- =============================================================================

-- Sample play by play data with game context (JOIN with game table)
SELECT
    pbp.*,
    g.game_date,
    g.season_id,
    g.season_type
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2020-01-01'
LIMIT 1000;

-- =============================================================================
-- PLAYER GAME AGGREGATION
-- =============================================================================

-- Create player-game level stats from play by play data
SELECT
    pbp.game_id,
    g.game_date,
    pbp.player1_id as player_id,
    pbp.player1_name as player_name,
    COUNT(*) as total_actions,
    SUM(CASE WHEN pbp.eventmsgtype = 1 THEN 1 ELSE 0 END) as field_goal_attempts,
    SUM(CASE WHEN pbp.eventmsgtype = 4 THEN 1 ELSE 0 END) as rebounds,
    SUM(CASE WHEN pbp.eventmsgtype = 5 THEN 1 ELSE 0 END) as turnovers,
    SUM(CASE WHEN pbp.eventmsgtype = 6 THEN 1 ELSE 0 END) as fouls
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE pbp.player1_id IS NOT NULL
  AND g.game_date >= '2020-01-01'
  AND pbp.player1_id = '{player_id}' -- Optional player filter
GROUP BY pbp.game_id, pbp.player1_id, pbp.player1_name, g.game_date
ORDER BY g.game_date DESC
LIMIT 100;

-- =============================================================================
-- HIGH USAGE PLAYER IDENTIFICATION
-- =============================================================================

-- Find players with high game frequency for workload analysis
SELECT
    pbp.player1_id,
    pbp.player1_name,
    COUNT(DISTINCT pbp.game_id) as games_played,
    COUNT(*) as total_actions,
    CAST(COUNT(*) AS FLOAT) / COUNT(DISTINCT pbp.game_id) as avg_actions_per_game
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE pbp.player1_id IS NOT NULL
  AND g.game_date >= '2020-01-01'
GROUP BY pbp.player1_id, pbp.player1_name
HAVING COUNT(DISTINCT pbp.game_id) >= 20 -- min_games threshold
ORDER BY total_actions DESC
LIMIT 50;

-- =============================================================================
-- DATE RANGE & TEMPORAL ANALYSIS
-- =============================================================================

-- Analyze date range and data distribution
SELECT
    MIN(game_date) as earliest_date,
    MAX(game_date) as latest_date,
    COUNT(*) as total_games,
    COUNT(DISTINCT season_id) as total_seasons
FROM game;

-- Games per year analysis
SELECT
    SUBSTR(game_date, 1, 4) as year,
    COUNT(*) as games_count
FROM game
GROUP BY SUBSTR(game_date, 1, 4)
ORDER BY year DESC
LIMIT 10;

-- =============================================================================
-- PERFORMANCE TESTING
-- =============================================================================

-- Test play by play JOIN performance
SELECT COUNT(*) as count
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2023-01-01';

-- =============================================================================
-- CLEAN DATA FILTERING
-- =============================================================================

-- Get clean player actions excluding technical/official events
SELECT
    pbp.*,
    g.game_date,
    g.season_id
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2020-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0' -- Excludes technical events
  AND pbp.player1_name IS NOT NULL
  AND pbp.player1_name != 'None' -- Double filter
LIMIT 1000;

-- =============================================================================
-- MODERN ERA DATA ANALYSIS
-- =============================================================================

-- Modern NBA era data volume check (2018+)
SELECT COUNT(*) as modern_records
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2018-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0';

-- Modern analytics era data (2015+) with comprehensive stats
SELECT
    COUNT(*) as total_records,
    COUNT(DISTINCT pbp.game_id) as unique_games,
    COUNT(DISTINCT pbp.player1_id) as unique_players,
    MIN(g.game_date) as earliest_date,
    MAX(g.game_date) as latest_date,
    COUNT(DISTINCT SUBSTR(g.game_date, 1, 4)) as seasons_covered
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0';

-- =============================================================================
-- MODELING CANDIDATE IDENTIFICATION
-- =============================================================================

-- Identify players with sufficient data for modeling
SELECT
    pbp.player1_id,
    pbp.player1_name,
    COUNT(DISTINCT pbp.game_id) as games_played,
    COUNT(*) as total_actions,
    CAST(COUNT(*) AS FLOAT) / COUNT(DISTINCT pbp.game_id) as avg_actions_per_game
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2018-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0'
GROUP BY pbp.player1_id, pbp.player1_name
HAVING COUNT(DISTINCT pbp.game_id) >= 50 -- min_games
   AND CAST(COUNT(*) AS FLOAT) / COUNT(DISTINCT pbp.game_id) >= 20 -- min_actions_per_game
ORDER BY total_actions DESC;

-- =============================================================================
-- YEARLY BREAKDOWN ANALYSIS
-- =============================================================================

-- Data distribution by year from 2015+
SELECT
    SUBSTR(g.game_date, 1, 4) as year,
    COUNT(*) as records,
    COUNT(DISTINCT pbp.game_id) as games,
    COUNT(DISTINCT pbp.player1_id) as players
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0'
GROUP BY SUBSTR(g.game_date, 1, 4)
ORDER BY year;

-- =============================================================================
-- PLAYER CONSISTENCY ANALYSIS
-- =============================================================================

-- Analyze player consistency for injury prediction modeling (2015+)
SELECT
    pbp.player1_id,
    pbp.player1_name,
    COUNT(DISTINCT SUBSTR(g.game_date, 1, 4)) as seasons_active,
    MIN(g.game_date) as first_game,
    MAX(g.game_date) as last_game,
    COUNT(DISTINCT pbp.game_id) as total_games,
    COUNT(*) as total_actions
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0'
GROUP BY pbp.player1_id, pbp.player1_name
HAVING COUNT(DISTINCT pbp.game_id) >= 100 -- Players with substantial data
ORDER BY total_actions DESC
LIMIT 20;

-- =============================================================================
-- INJURY/ABSENCE PATTERN ANALYSIS
-- =============================================================================

-- Identify potential injury periods by finding gaps in game activity
WITH player_games AS (
    SELECT DISTINCT
        g.game_date,
        pbp.player1_name
    FROM play_by_play pbp
    JOIN game g ON pbp.game_id = g.game_id
    WHERE pbp.player1_id = '203507' -- Player ID parameter
      AND g.game_date >= '2015-01-01'
    ORDER BY g.game_date
),
game_gaps AS (
    SELECT
        game_date,
        player1_name,
        LAG(game_date) OVER (ORDER BY game_date) as prev_game,
        julianday(game_date) - julianday(LAG(game_date) OVER (ORDER BY game_date)) as days_gap
    FROM player_games
)
SELECT *
FROM game_gaps
WHERE days_gap >= 7 -- min_gap_days parameter
ORDER BY days_gap DESC;

-- =============================================================================
-- DATA VOLUME ANALYSIS (VARIOUS ERAS)
-- =============================================================================

-- 2000+ Era Data Volume
SELECT
    COUNT(*) as total_records,
    COUNT(DISTINCT pbp.game_id) as unique_games,
    COUNT(DISTINCT pbp.player1_id) as unique_players,
    MIN(g.game_date) as earliest_date,
    MAX(g.game_date) as latest_date
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2000-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0';

-- 2015+ Era Data Volume
SELECT
    COUNT(*) as total_records,
    COUNT(DISTINCT pbp.game_id) as unique_games,
    COUNT(DISTINCT pbp.player1_id) as unique_players,
    MIN(g.game_date) as earliest_date,
    MAX(g.game_date) as latest_date
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0';

-- =============================================================================
-- EVENT TYPES DISTRIBUTION ANALYSIS
-- =============================================================================

-- Event types distribution for feature engineering (2015+)
SELECT
    eventmsgtype,
    COUNT(*) as event_count,
    ROUND(COUNT(*) * 100.0 / (
        SELECT COUNT(*) 
        FROM play_by_play pbp
        JOIN game g ON pbp.game_id = g.game_id
        WHERE g.game_date >= '2015-01-01'
    ), 2) as percentage
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0'
GROUP BY eventmsgtype
ORDER BY event_count DESC;

-- =============================================================================
-- DATA QUALITY ASSESSMENT
-- =============================================================================

-- Data completeness and quality check (2015+)
SELECT
    'Total Records' as metric,
    COUNT(*) as value
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'

UNION ALL

SELECT
    'Records with Player ID' as metric,
    COUNT(*) as value
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_id IS NOT NULL
  AND pbp.player1_id != '0'

UNION ALL

SELECT
    'Records with Player Name' as metric,
    COUNT(*) as value
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_name IS NOT NULL
  AND pbp.player1_name != ''

UNION ALL

SELECT
    'Records with Team Info' as metric,
    COUNT(*) as value
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
  AND pbp.player1_team_id IS NOT NULL;

-- =============================================================================
-- DETAILED PLAYER ACTION ANALYSIS
-- =============================================================================

-- Deep dive into specific player's recent actions (e.g., Giannis)
SELECT
    game_date,
    eventmsgtype,
    eventmsgactiontype,
    period,
    pctimestring,
    homedescription,
    visitordescription,
    neutraldescription
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2022-01-01'
  AND pbp.player1_id = '203507' -- Giannis player ID
ORDER BY game_date DESC, eventnum
LIMIT 50;
