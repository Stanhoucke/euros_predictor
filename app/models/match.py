class Match():
    def __init__(self, team_1, team_2, id=None):
        self.team_1 = team_1
        self.team_2 = team_2
        self.goals = {"home": None, "away": None}
        self.id = id
        
    def set_goals(self, home_goals, away_goals):
        self.goals["home"] = home_goals
        self.goals["away"] = away_goals