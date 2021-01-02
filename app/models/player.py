class Player():
    def __init__(self, email, password, first_name, last_name, team_name, points=0, id=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.team_name = team_name
        self.points = points
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        