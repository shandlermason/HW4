# Handle settings
import math


def coerce():
    pass


def cli():
    pass


# Lists 
def copy(t):
    """Deep Copy"""
    if(type(t) == 'dict'):
        u = {}
        for k,v in t.items():
            u[k] = v
        return u

    # assume t is a list 
    u = []
    for x in t:
        u.append(x)
    return u
    
        

def per(t, p=0.5):
    """Return the pth thing from the sorted list t"""
    p = math.floor(p*len(t)+0.5)
    p = p - 1
    return t[max(0, min(len(t)-1, p))]

def push(t, x):
    kys = sorted(t.keys())
    pos = len(kys)
    t[pos] = x
    return x

def csv():
    pass


# Strings
def o():
    pass

def oo():
    pass


# Miscs

def rouges():
    pass


# Maths
def rnd():
    pass


if __name__ == "__main__":
    # t = {
    #     "h": 10,
    #     "z": 27,
    #     "abc": {"1": 10}
    # }
    
    # t = [1,2,3,4,5]
    
    # print(t)
    # u = copy(t)
    # print(u)
    # print(t == u)
    
    t = {0: 1, 1: 2,2: 3, 3: 4,4: 5,5: 6}
    
    print(per(t,-2))
    
    print(t)
    
    push(t, 20)
    print(t)
    
    