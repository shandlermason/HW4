# from code import main
# from code.main import Num
from code.sym import Sym
# import unittest

# class TestCases(unittest.TestCase):
#     def test_num(self):
#         num = Num(1, "name")
#         mid = num.mid()
#         div = num.div()
#         print(mid, div)
def test_sym():
    sym=Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode=sym.mid()
    entropy=sym.div()
    #print(mode,entropy) #oo has to be implemented later
    assert mode=='a' and (entropy>=1.37 and entropy<=1.38)
