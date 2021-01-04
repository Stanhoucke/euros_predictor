class Prediction():
    def __init__(self, player, match, goals={"home": None, "away": None}, id=None):
        self.player = player
        self.match = match
        self.goals = goals

    def team_points(self):
        if self.goals["home"] > self.goals["away"]:
            self.match.team_1.group_info["points"] += 3
        elif self.goals["away"] > self.goals["home"]:
            self.match.team_2.group_info["points"] += 3
        else:
            self.match.team_1.group_info["points"] += 1
            self.match.team_2.group_info["points"] += 1

