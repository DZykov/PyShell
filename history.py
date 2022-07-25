import settings


class History:


    def __init__(self):
        self.src = settings.PATH_SRC
        self.history = []
        self.load_src()


    def load_src(self):
        lines = []
        with open(self.src) as f:
            lines = f.readlines()
        self.history = lines[:settings.HISTORY_MAX]
    
    
    def write_src(self, cmd):
        pass


    def add(self, cmd):
        pass


    def delete(self, cmd):
        pass


    def get_last(self):
        pass