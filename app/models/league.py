from random import randrange

class League():
    def __init__(self, name, join_code, id=None):
        self.name = name
        self.join_code = join_code
        self.id = id

    def generate_join_code(self):
        join_code = randrange(99999999)
        
        # Convert int to str padding to 8 characters
        str_join_code = f"{join_code:08}"
        str_join_code.insert(4,"-")
        return str_join_code
