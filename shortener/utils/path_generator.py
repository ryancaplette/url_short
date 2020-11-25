import random
import string

class ShortPath:
    path_length = 6

    def __init__(self):
        pass
    
    def gen_path(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.path_length))