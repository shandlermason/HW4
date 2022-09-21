# from code import main
import os
import sys
from code.Num import Num
from code.Sym import Sym
# from code.data import Data
from code.utils import oo,csv
import code.settings as settings

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

def test_the():
    oo(settings.the)
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
    print('\n', ':div', entropy, ':mid', mode)

    assert mode == 'a' and (1.37 <= entropy <= 1.38)


def test_bignum():
    num = Num()
    settings.the["nums"] = 32
    for i in range(1, 1001):
        num.add(i)
    print('\n', num.nums())
    assert 32 == len(num._has)



def test_csv():
    global n
    n = 0
    print('\n')
    def func_row(row):
        global n
        n = n + 1
        if n > 10:
            return n
        else:
            return oo(row)
    
    csv(f'{PROJECT_DIR}/data/auto93.csv', func_row)


def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    fail_count += test_bignum()
    fail_count += test_sym()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
