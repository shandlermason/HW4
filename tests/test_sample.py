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
# import math

# class Sym:
#     def __init__(self, c=0, s=""):
#         self.n = 0
#         self.at = c 
#         self.name = s 
#         self._has = dict()
        
#     def add(self,v):
#         if (v != "?"):
#             self.n = self.n + 1
#             if v in self._has:
#                 self._has[v] = 1 + self._has[v]
#             else: self._has[v] = 1

#     def mid(self,col=0,most=-1,mode=""):
#         most=-1
#         for k,v in self._has.items():
#             if v > most:
#                 mode=k
#                 most=v
#         return mode

#     def div(self,e=0):
#         def fun(p):
#             return p*math.log(p,2)
#         e=0
#         for _,n in self._has.items():
#             if n>0:
#                 e=e-fun(n/self.n)
#         return e

def test_sym():
    sym=Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode=sym.mid()
    entropy=sym.div()
    #print(mode,entropy) #oo has to be implemented later
    assert mode=='a' #and (entropy>=1.37 and entropy<=1.38)
