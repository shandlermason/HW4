class Row:
    def __init__(self, t):
        self.cells = t
        # self.cooked = copy(t) # copy function needs to be implemented
        self.isEvaled = False
