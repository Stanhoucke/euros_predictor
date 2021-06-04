class Prediction():
    def __init__(self, player, match, home_player_team, away_player_team, id=None):
        self.player = player
        self.match = match
        self.home_player_team = home_player_team
        self.away_player_team = away_player_team
        self.goals = {"home": None, "away": None}
        self.id = id

    def set_goals(self, home_goals, away_goals):
        self.goals["home"] = home_goals
        self.goals["away"] = away_goals

    # Team updates
    def team_goals(self):
        # Home team
        if self.goals["home"] is not None:
            self.home_player_team.group_info["for"] += self.goals["home"]
            self.home_player_team.group_info["against"] += self.goals["away"]
            self.home_player_team.group_info["difference"] = self.home_player_team.group_info["for"] - self.home_player_team.group_info["against"]
            self.home_player_team.group_info["played"] += 1

        # Away team
        if self.goals["away"] is not None:
            self.away_player_team.group_info["for"] += self.goals["away"]
            self.away_player_team.group_info["against"] += self.goals["home"]
            self.away_player_team.group_info["difference"] = self.away_player_team.group_info["for"] - self.away_player_team.group_info["against"]
            self.away_player_team.group_info["played"] += 1

    def team_points(self):
        if self.goals["home"] is not None and self.goals["away"] is not None:
            if self.goals["home"] > self.goals["away"]:
                self.home_player_team.group_info["points"] += 3
                self.home_player_team.group_info["won"] += 1
                self.away_player_team.group_info["lost"] += 1
            elif self.goals["away"] > self.goals["home"]:
                self.away_player_team.group_info["points"] += 3
                self.away_player_team.group_info["won"] += 1
                self.home_player_team.group_info["lost"] += 1
            else:
                self.home_player_team.group_info["points"] += 1
                self.away_player_team.group_info["points"] += 1
                self.home_player_team.group_info["drawn"] += 1
                self.away_player_team.group_info["drawn"] += 1

    def update_team_stats(self):
        self.team_goals()
        self.team_points()

    # Match outcome based points
    def predicted_outcome(self):
        if self.goals["home"] > self.goals["away"]:
            return "w"
        elif self.goals["home"] == self.goals["away"]:
            return "d"
        else:
            return "l"

    def actual_outcome(self):
        if self.match.goals["home"] > self.match.goals["away"]:
            return "w"
        elif self.match.goals["home"] == self.match.goals["away"]:
            return "d"
        else:
            return "l"

    def outcome_points(self):
        if self.predicted_outcome() == self.actual_outcome():
            self.player.points += 3

    # Goals based points
    def home_goals_correct(self):
        return self.goals["home"] == self.match.goals["home"]
    
    def away_goals_correct(self):
        return self.goals["away"] == self.match.goals["away"]

    def goals_points(self):
        if self.home_goals_correct() and self.away_goals_correct():
            self.player.points += 2
        elif self.home_goals_correct() or self.away_goals_correct():
            self.player.points += 1

    # Award player points
    def award_points(self):
        self.outcome_points()
        self.goals_points()
    
    # Match played
    def match_played(self):
        self.update_team_stats()
        self.award_points()