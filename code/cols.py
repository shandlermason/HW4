import re
from code.num import Num
from code.sym import Sym


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}

        skipped_columns = []
        for c, s in enumerate(names):

            match = re.findall(":$", s)
            if match:
                skipped_columns.append(s)

            if re.findall("[A-Z]", s):
                col = Num(c, s)
                self.all[c] = col
                if s not in skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y[c] = col
                    else:
                        self.x[c] = col
            else:
                col = Sym(c, s)
                self.all[c] = col
                if s not in skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y[c] = col
                    else:
                        self.x[c] = col

            # not sure if this is in the right spot
            if re.findall("!$", s):
                self.klass = col
