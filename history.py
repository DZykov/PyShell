import settings


class History:


    def __init__(self):
        self.src = settings.HISTORY_SRC
        self.history = []
        self.load_src()


    def load_src(self):
        lines = []
        with open(self.src, 'r') as f:
            for line in f:
                self.history.insert(0, line[:-1])
    
    
    def write_src(self):
        with open(self.src, 'w') as f:
            for cmd in self.history:
                f.write("%s\n" % cmd)


    def add(self, cmd):
        self.history.insert(0, cmd)
        if len(self.history) == settings.HISTORY_MAX:
            self.history.pop()
        self.write_src()     


    def delete(self, cmd):
        self.history.pop()
        self.write_src()


    def get_last(self):
        self.load_src()
        if len(self.history) > 0:
            return self.history[0]
        return None