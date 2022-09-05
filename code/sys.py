def mid(self,col,most,mode):
    most=-1
    for k,v in self._has.items():
        if v > most:
            mode=k
            most=v
    return mode

def div(self,e,fun):
    def fun(p):
        return p*math.log(p,2)
    e=0
    for _,n in self._has.items():
        if n>0:
            e=e-fun(n/self.n)
    return e
