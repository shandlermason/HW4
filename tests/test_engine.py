import os
import sys
from src.num import Num
from src.sym import Sym
from src.data import Data
from src import utils



def test_the():
    if utils.the:
        print('\n', utils.the)
        return True
    else:
        print('the does not exist')


def test_num():
    num = Num()
    for i in range(1, 101):
        num.add(i)
    mid, div = num.mid(), num.div()
    print('\n', mid, div)
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
    utils.the["nums"] = 32
    for i in range(1, 1001):
        num.add(i)
    print('\n', num.nums())
    assert 32 == len(num._has)
    utils.the['nums'] = 512


def test_csv():
    rows = utils.csv_function('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    print('\n')
    for line in rows[0:10]:
        print(line)
    assert len(rows) != 0


def test_data():
    d = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')
    print('\n')
    for col in d.cols.y:
        dd = d.cols.y[col].__dict__
        print(':at', dd['at'], ':hi', dd['hi'], ':isSorted', dd['isSorted'], ':lo', dd['lo'], ':n', dd['n'],
              ':name', dd['name'], ':w', dd['w'])
    assert d.cols.y is not None


def test_stats():
    data = Data('https://raw.githubusercontent.com/timm/lua/main/data/auto93.csv')

    def mid(col):
        if isinstance(col, Num):  # type check, if col is an instance of 'Num'
            return Num.mid(col)
        else:
            return Sym.mid(col)

    def div(col):
        if isinstance(col, Num):
            return Num.div(col)
        else:
            return Sym.div(col)

    print('\n')
    print("xmid", data.stats(2, data.cols.x, mid))
    print("xdiv", data.stats(3, data.cols.x, div))
    print("ymid", data.stats(2, data.cols.y, mid))
    print("ydiv", data.stats(3, data.cols.y, div))


def main():
    fail_count = 0
    fail_count += test_the()
    fail_count += test_num()
    fail_count += test_bignum()
    fail_count += test_sym()
    fail_count += test_csv()
    fail_count += test_data()
    fail_count += test_stats()
    return fail_count  # 0 is Success


if __name__ == "__main__":
    main()
