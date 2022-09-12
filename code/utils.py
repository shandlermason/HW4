# Handle settings
def coerce():
    pass


def cli():
    pass


# Lists 
def copy(t):
    u = {}
    for k,v in t.items():
        u[k] = v
    return u
        

def per():
    pass

def push():
    pass

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
    t = {
        "h": 10,
        "z": 27,
        "abc": {"1": 10}
    }
    
    print(t)
    u = copy(t)
    print(u)
    print(t == u)