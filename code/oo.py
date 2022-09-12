# %%
def o(t, show, u):
    print_str = "{}"
    len = len(t)
    if type(t) != dict:
        return str(t)
    def show(k, v):
        if not str(k): #find"^_"??
            v = o(v)
            return len(t)==0 and print_str.format(k, v) or str(v)
    u = dict()
    for k, v in t:
        u[1+len(u)] = show(k, v)
    if len(t) == 0:
        sorted(u)
    return ("{" + u + " }")

def oo(t):
    print(o(t))
    return t
