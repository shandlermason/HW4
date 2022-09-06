from distutils import ccompiler


def func(x):
    return x + 1

class Sym:
    def __init__(self, c = 0, s = ""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        
    
    def add(v, self=None):
        if (v != "?"):
            self.n = self.n + 1
            self._has[v] = 1 + (self._has[v]) #v or 0



class Num:

    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True
        
        # self.w
        
    def nums(self):
        """Return kept numbers sorted"""
        if not self.isSorted:
            self._has.sort()
            self.isSorted = True
        return self._has

    def add(self):
        return 0

    # standard deviation
    def div(self):
        percentile_90 = 0.90 * self # find 90th percentile
        percentile_10 = 0.10 * self # find 10th percentile
        return (percentile_90-percentile_10) / 2.56 # return (90th-10th)/2.56


    def mid(self):
        return self.x  # median - sort numbers seen so far, return the middle value
