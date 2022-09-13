from distutils import ccompiler
from code.utils import per
import math
# from code.gv import the
import random

the = {"nums":512}
import re

class Num:

    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = float('inf')
        self.hi = float('-inf')
        self.isSorted = True
        self.w = -1 if re.search('-$', s) else 1

    def nums(self):
        """Return kept numbers sorted"""
        if not self.isSorted:
            # self._has.sort()
            sorted(self._has.items(), key=lambda x: x[1])
            self.isSorted = True
        return self._has

    def add(self, v, pos = 0):
        if v!="?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the["nums"]:
                pos = len(self._has)
            elif random.random() < the["nums"]/self.n:
                pos = random.randint(1,len(self._has)-1)
            if pos >= 0:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        a = list(self.nums().values())
        # percentile_90 = 0.90 * self.nums()  # find 90th percentile
        # percentile_10 = 0.10 * self.nums()  # find 10th percentile
        # return (percentile_90 - percentile_10) / 2.58  # return (90th-10th)/2.56
        return ( per(a, .9) - per(a, .1) ) / 2.58

    def mid(self):
        sorted_num = list(self.nums().values())
        
        len_of_list = len(sorted_num)

        if len_of_list > 0:
            if len_of_list % 2 == 0:
                first_median = sorted_num[len_of_list // 2]
                second_median = sorted_num[len_of_list // 2 - 1]
                mid = (first_median + second_median) / 2
            else:
                mid = sorted_num[len_of_list // 2]
            return mid


if __name__ == "__main__":
    num = Num()
    print(num._has)
    
    for i in range(1,100):
        num.add(i)
        
    print(num._has)
    
    num.div()
