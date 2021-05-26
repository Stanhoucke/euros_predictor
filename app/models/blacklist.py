import datetime

class Blacklist():
    def __init__(self, token):
        self.token = token
        self.blacklist_date = datetime.datetime.now()
