class Prediction():
    def __init__(self, player, match, goals={"home": None, "away": None}, id=None):
        self.player = player
        self.match = match
        self.goals = goals

    def team_goals(self):
        # Home team
        self.match.team_1.group_info["for"] += self.goals["home"]
        self.match.team_1.group_info["against"] += self.goals["away"]
        self.match.team_1.group_info["difference"] = self.match.team_1.group_info["for"] - self.match.team_1.group_info["against"]
        self.match.team_1.group_info["played"] += 1

        # Away team
        self.match.team_2.group_info["for"] += self.goals["away"]
        self.match.team_2.group_info["against"] += self.goals["home"]
        self.match.team_2.group_info["difference"] = self.match.team_1.group_info["for"] - self.match.team_1.group_info["against"]
        self.match.team_2.group_info["played"] += 1

    def team_result(self):
        if self.goals["home"] > self.goals["away"]:
            self.match.team_1.group_info["points"] += 3
            self.match.team_1.group_info["won"] += 1
            self.match.team_2.group_info["lost"] += 1
        elif self.goals["away"] > self.goals["home"]:
            self.match.team_2.group_info["points"] += 3
            self.match.team_2.group_info["won"] += 1
            self.match.team_1.group_info["lost"] += 1
        else:
            self.match.team_1.group_info["points"] += 1
            self.match.team_2.group_info["points"] += 1
            self.match.team_1.group_info["drawn"] += 1
            self.match.team_2.group_info["drawn"] += 1

    def play_match(self):
        self.team_goals()
        self.team_result()
