from db.run_sql import run_sql
from models.team import Team

# Create
def save(team):
    sql = "INSERT INTO teams (name, matches_played, won, drawn, lost, goals_for, goals_against, goal_difference, points, group_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.group_info["played"], team.group_info["won"], team.group_info["drawn"], team.group_info["lost"], team.group_info["for"], team.group_info["against"], team.group_info["difference"], team.group_info["points"], team.group_info["rank"]]
    result = run_sql(sql, values)
    team.id = result[0]['id']
    return team

# Read
def select(id):
    team = None

    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        group_info = {
            "played": result['matches_played'],
            "won": result['won'],
            "drawn": result['drawn'],
            "lost": result['lost'],
            "for": result['goals_for'],
            "against": result['goals_against'],
            "difference": result['goal_difference'],
            "points": result['points'],
            "rank": result['group_rank']
        }
        team = Team(result['name'], group_info, result['id'])
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        group_info = {
            "played": row['matches_played'],
            "won": row['won'],
            "drawn": row['drawn'],
            "lost": row['lost'],
            "for": row['goals_for'],
            "against": row['goals_against'],
            "difference": row['goal_difference'],
            "points": row['points'],
            "rank": row['group_rank']
        }
        team = Team(row['name'], group_info, row['id'])
        teams.append(team)
    return teams

# Update
def update(team):
    sql = "UPDATE teams SET (name, matches_played, won, drawn, lost, goals_for, goals_against, goal_difference, points, group_rank) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.group_info["played"], team.group_info["won"], team.group_info["drawn"], team.group_info["lost"], team.group_info["for"], team.group_info["against"], team.group_info["difference"], team.group_info["points"], team.group_info["rank"], team.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)
