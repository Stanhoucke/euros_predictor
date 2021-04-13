class PlayerPoints():
    def __init__(self, prediction, result, id=None):
        self.prediction = prediction
        self.result = result
        self.id = id
    
    # Match outcome based points
    def predicted_outcome(self):
        if self.prediction.goals["home"] > self.prediction.goals["away"]:
            return "w"
        elif self.prediction.goals["home"] == self.prediction.goals["away"]:
            return "d"
        else:
            return "l"

    def actual_outcome(self):
        if self.result.goals["home"] > self.result.goals["away"]:
            return "w"
        elif self.result.goals["home"] == self.result.goals["away"]:
            return "d"
        else:
            return "l"

    def outcome_points(self):
        if self.predicted_outcome() == self.actual_outcome():
            self.prediction.player.points += 3

    # Goals based points
    def home_goals_correct(self):
        return self.prediction.goals["home"] == self.result.goals["home"]
    
    def away_goals_correct(self):
        return self.prediction.goals["away"] == self.result.goals["away"]

    def goals_points(self):
        if self.home_goals_correct() and self.away_goals_correct():
            self.prediction.player.points += 2
        elif self.home_goals_correct() or self.away_goals_correct():
            self.prediction.player.points += 1

    # Award player points
    def award_points(self):
        self.outcome_points()
        self.goals_points()
        