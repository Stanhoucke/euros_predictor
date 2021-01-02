DROP TABLE player_points;
DROP TABLE results;
DROP TABLE predictions;
DROP TABLE matches;
DROP TABLE groups;
DROP TABLE player_leagues;
DROP TABLE players;
DROP TABLE leagues;
DROP TABLE teams;

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

CREATE TABLE player_leagues (
    id SERIAL PRIMARY KEY,
    league_id INT REFERENCES leagues(id) ON DELETE CASCADE,
    player_id INT REFERENCES players(id) ON DELETE CASCADE
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
    team_1_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    match_id INT REFERENCES matches(id) ON DELETE CASCADE,
    team_1_goals INT,
    team_2_goals INT
);

CREATE TABLE results (
    id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches(id) ON DELETE CASCADE,
    team_1_goals INT,
    team_2_goals INT
);

CREATE TABLE player_points (
    id SERIAL PRIMARY KEY,
    prediction_id INT REFERENCES predictions(id) ON DELETE CASCADE,
    result_id INT REFERENCES results(id) ON DELETE CASCADE
);