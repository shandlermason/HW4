from distutils import ccompiler
import math

# def func(x):
    # return x + 1

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

#     def add(self, v, pos):
#         if v!="?":
#             self.n = self.n + 1
#             self.lo = math.min(v, self.lo)
#             self.hi = math.max(v, self.hi)
#             if len(self._has) < the.nums:
#                 pos = 1 + len(self._has)
#             elif math.random() < the.nums/self.n:
#                 pos = math.random(len(self._has))
#             if pos:
#                 self.isSorted = False
#                 self._has[pos] = int(v)

    def div(self):
        percentile_90 = 0.90 * self.nums()  # find 90th percentile
        percentile_10 = 0.10 * self.nums()  # find 10th percentile
        return (percentile_90 - percentile_10) / 2.58  # return (90th-10th)/2.56

    def mid(self):
        sorted_num = self.nums()
        len_of_list = len(sorted_num)
        if len_of_list % 2 == 0:
            first_median = sorted_num[len_of_list // 2]
            second_median = sorted_num[len_of_list // 2 - 1]
            mid = (first_median + second_median) / 2
        else:
            mid = sorted_num[len_of_list // 2]
        return mid
