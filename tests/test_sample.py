# from code import main
from code.Num import Num
from code.Sym import Sym
from code.data import Data
from code.utils import oo

def test_the():
    assert True


def test_num():
    num = Num()
    for i in range(1, 101):
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


def test_bignum():
    return 0  # assert goes here

# def test_csv(n):
#     n = 0


# def test_data(d):
#     d = Data()


# def test_stats(data, mid, div):
#     data = Data()