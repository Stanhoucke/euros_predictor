from random import randrange

class League():
    def __init__(self, name, join_code, id=None):
        self.name = name
        self.join_code = join_code
        self.id = id

    def generate_join_code(self):
        generated_code = randrange(99999999)
        
        # Convert int to str padding to 8 characters
        str_code = f"{generated_code:08}"
        join_code = str_code[:4] + "-" + str_code[4:]
        return join_code
