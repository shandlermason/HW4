# from code import main
from code.main import Num
# import unittest
from code.sym import Sym

# class TestCases(unittest.TestCase):
#     def test_num(self):
#         num = Num(1, "name")
#         mid = num.mid()
#         div = num.div()
#         print(mid, div)

import math


def test_num():
    num = Num()
    for i in range(0, 100):
        num.add(i)
    mid, div = num.mid(), num.div()
    print(mid, div)
    assert (50 <= mid <= 52) and (30.5 < div < 32)


def test_sym():
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    # print(mode,entropy) #oo has to be implemented later
    assert mode == 'a' and (1.37 <= entropy <= 1.38)
