-- =============================================================================
-- TOP PLAYER IDENTIFICATION
-- =============================================================================

-- Find top 20 players with 100+ games for modeling
SELECT
    pbp.player1_id,
    pbp.player1_name,
    COUNT(DISTINCT pbp.game_id) as games_played,
    COUNT(*) as total_actions,
    MIN(g.game_date) as first_game,
    MAX(g.game_date) as last_game,
    COUNT(DISTINCT SUBSTR(g.game_date, 1, 4)) as seasons_active
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
AND pbp.player1_id IS NOT NULL
AND pbp.player1_id != '0'
GROUP BY pbp.player1_id, pbp.player1_name
HAVING COUNT(DISTINCT pbp.game_id) >= 100
ORDER BY total_actions DESC
LIMIT 20;

-- =============================================================================
-- PLAYER-GAME LEVEL DATA EXTRACTION
-- =============================================================================

-- Load player-game level data for top players with event breakdowns
SELECT
    pbp.game_id,
    g.game_date,
    pbp.player1_id as player_id,
    pbp.player1_name as player_name,
    g.season_id,
    g.season_type,
    
    -- Total activity metrics
    COUNT(*) as total_actions,
    
    -- Event type breakdowns (based on EDA findings)
    -- Shooting Load (Types 1+2+3 = 37.4% of actions)
    SUM(CASE WHEN pbp.eventmsgtype = 1 THEN 1 ELSE 0 END) as made_shots,
    SUM(CASE WHEN pbp.eventmsgtype = 2 THEN 1 ELSE 0 END) as missed_shots,  
    SUM(CASE WHEN pbp.eventmsgtype = 3 THEN 1 ELSE 0 END) as free_throws,
    
    -- Defensive Load (Type 4 = 22.5% of actions)
    SUM(CASE WHEN pbp.eventmsgtype = 4 THEN 1 ELSE 0 END) as rebounds,
    
    -- Physical Contact Load (Types 6+3 = 18.7%)
    SUM(CASE WHEN pbp.eventmsgtype = 6 THEN 1 ELSE 0 END) as fouls,
    
    -- Ball Handling Stress (Type 5 = 6.1%)
    SUM(CASE WHEN pbp.eventmsgtype = 5 THEN 1 ELSE 0 END) as turnovers,
    
    -- Substitution tracking (Type 8 = 9.8%)
    SUM(CASE WHEN pbp.eventmsgtype = 8 THEN 1 ELSE 0 END) as substitutions,
    
    -- Other events
    SUM(CASE WHEN pbp.eventmsgtype NOT IN (1,2,3,4,5,6,8) THEN 1 ELSE 0 END) as other_events
    
FROM play_by_play pbp
JOIN game g ON pbp.game_id = g.game_id
WHERE g.game_date >= '2015-01-01'
AND g.game_date <= '2023-06-12'
AND pbp.player1_id IN ('{player_ids}')
AND pbp.player1_id IS NOT NULL
AND pbp.player1_id != '0'
AND g.season_type = 'Regular Season'  -- Focus on regular season for consistency
GROUP BY pbp.game_id, pbp.player1_id, pbp.player1_name, g.game_date, g.season_id, g.season_type
ORDER BY pbp.player1_id, g.game_date;

-- =============================================================================
-- PLAYER CONTEXT DATA EXTRACTION
-- =============================================================================

-- Load player biographical and career context data
SELECT 
    person_id as player_id,
    display_first_last as player_name,
    birthdate,
    height,
    weight,
    season_exp,
    position,
    draft_year,
    draft_round,
    draft_number,
    from_year,
    to_year
FROM common_player_info
WHERE person_id IN ('{player_ids}');