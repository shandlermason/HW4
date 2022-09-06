from code import main
from code.main import Num
from code.sym import Sym
import unittest

def test_answer():
    assert main.func(3) == 5


class TestCases(unittest.TestCase):
    def test_num(self):
        num = Num(1, "name")
        mid = num.mid()
        div = num.div()
        print(mid, div)