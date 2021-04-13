class Result():
    def __init__(self, match, goals={"home": None, "away": None}, id=None):
        self.match = match
        self.goals = goals

    # def team_points(self):
    #     if self.team_1_goals > self.team_2_goals:
    #         self.match.team_1.group_info["points"] += 3
    #     elif self.team_2_goals > self.team_1_goals:
    #         self.match.team_2.group_info["points"] += 3
    #     else:
    #         self.match.team_1.group_info["points"] += 1
    #         self.match.team_2.group_info["points"] += 1

