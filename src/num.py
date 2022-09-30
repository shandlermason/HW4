
import math
# from src.gv import the
import random
from src import utils

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
            self._has = sorted(self._has.values())  # sort by value
            self.isSorted = True
        return self._has

    def add(self, v, pos=0):
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < utils.the["nums"]:
                pos = len(self._has)
            elif random.random() < utils.the["nums"]/self.n:
                pos = random.randint(1,len(self._has)-1)
            if pos >= 0:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        a = self.nums()
        return (utils.per(a, .9) - utils.per(a, .1)) / 2.58

    def mid(self):
        sorted_num = self.nums()
        
        len_of_list = len(sorted_num)

        if len_of_list > 0:
            if len_of_list % 2 == 0:
                first_median = sorted_num[len_of_list // 2]
                second_median = sorted_num[len_of_list // 2 - 1]
                mid = (first_median + second_median) / 2
            else:
                mid = sorted_num[len_of_list // 2]
            return mid
