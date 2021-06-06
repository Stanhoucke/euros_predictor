DROP TABLE predictions;
DROP TABLE matches;
DROP TABLE groups;
DROP TABLE player_groups;
DROP TABLE player_leagues;
DROP TABLE player_teams;
DROP TABLE teams;
DROP TABLE players;
DROP TABLE leagues;
DROP TABLE blacklist_tokens;


CREATE TABLE leagues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    join_code VARCHAR(9)
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    team_name VARCHAR(255),
    points INT
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    matches_played INT,
    won INT,
    drawn INT,
    lost INT,
    goals_for INT,
    goals_against INT,
    goal_difference INT,
    points INT,
    group_rank INT
);

CREATE TABLE player_teams (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    matches_played INT,
    won INT,
    drawn INT,
    lost INT,
    goals_for INT,
    goals_against INT,
    goal_difference INT,
    points INT,
    group_rank INT
);

CREATE TABLE player_leagues (
    id SERIAL PRIMARY KEY,
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE,
    player_id INT REFERENCES players(id) ON DELETE CASCADE
);

CREATE TABLE player_groups (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    name VARCHAR(1),
    team_1_id INT REFERENCES player_teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES player_teams(id) ON DELETE CASCADE,
    team_3_id INT REFERENCES player_teams(id) ON DELETE CASCADE,
    team_4_id INT REFERENCES player_teams(id) ON DELETE CASCADE
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(1),
    team_1_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_3_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_4_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    round_number VARCHAR(255),
    date TIMESTAMP,
    location VARCHAR(255),
    group_name VARCHAR(255),
    team_1_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES teams(id) ON DELETE CASCADE,
    home_goals INT,
    away_goals INT
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    match_id INT REFERENCES matches(id) ON DELETE CASCADE,
    team_1_id INT REFERENCES player_teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES player_teams(id) ON DELETE CASCADE,
    home_goals INT,
    away_goals INT,
    has_prediction BOOLEAN
);

CREATE TABLE blacklist_tokens (
    id SERIAL PRIMARY KEY,
    token VARCHAR(255),
    blacklist_date TIMESTAMP
);
