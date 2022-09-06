import re


class Cols:
    def __init__(self, names):
        self.names = names
        self.all = {}
        self.klass = None
        self.x = {}
        self.y = {}

        for c, s in names:
            self.all = re.findall("^[A-Z]*", s)  # checks if column header starts with capital letter
            skipped_columns = re.findall(":$", s)  # checks if column header ends in colon

            if re.findall("[!+-]", s):
                self.y[""].append(s)  # dependent columns (have symbols)
            else:
                self.x[""].append(s)  # independent columns (no symbols)
