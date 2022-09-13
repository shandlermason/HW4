import re
from code.Num import Num
from code.Sym import Sym


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}

        for c, s in names:

            skipped_columns = re.findall(":$", s)  # checks if column header ends in colon

            if re.findall("[A-Z]", s):  # checks if column header starts with capital letter
                col = Num(c, s)
                self.all.update(col)
                if not skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y.update(col)  # dependent columns (have symbols)
                    else:
                        self.x.update(col)  # independent columns (no symbols)
            else:
                col = Sym(c, s)
                self.all.update(col)
                if not skipped_columns:
                    if re.findall("[!+-]", s):
                        self.y.update(col)  # dependent columns (have symbols)
                    else:
                        self.x.update(col)  # independent columns (no symbols)

            # not sure if this is in the right spot
            if re.findall("!$", s):
                self.klass = col
