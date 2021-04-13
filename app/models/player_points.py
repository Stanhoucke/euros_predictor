class PlayerPoints():
    def __init__(self, prediction, result, id=None):
        self.prediction = prediction
        self.result = result
        self.id = id
    
    def predicted_outcome(self):
        # Was home win, loss or draw predicted
        if self.prediction.goals["home"] > self.prediction.goals["away"]:
            return "w"
        elif self.prediction.goals["home"] == self.prediction.goals["away"]:
            return "d"
        else:
            return "l"

    def actual_outcome(self):
        # Did home actually win, lose, draw
        pass

    def outcome_points(self):
        # Points given based on match outcome
        pass

    def home_goals_points(self):
        # Did player predicted correct number of home goals
        pass
    
    def away_goals_points(self):
        # Did player predicted correct number of away goals
        pass

    def award_points(self):
        pass
        