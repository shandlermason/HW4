import re

help = """
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
USAGE: lua seen.lua [OPTIONS]

OPTIONS:
-e --eg start-up example = nothing
-d --dump on test failure, exit with stack dump = false
-f --file file with csv data = ../data/auto93.csv
-h --help show help = false
-n --nums number of nums to keep = 512
-s --seed random number seed = 10019
-S --seperator feild seperator = ,"""

def coerce(s):
    def fun(s1):
        if s1=="true":
            return True 
        if s1=="false":
            return False  
        return s1
    return int(s) or fun(re.search("^\s*(.-)\s*$",s)) #edit the parameter of fun

the = {}
# print(help)
print(type(help))
# tuples = re.findall(r'--(.*)\s=\s(.*)', help)
# print(tuples)
tuples = re.findall("[-][\S][\s][-][-]([\S]+)[^\n]+= ([\S]+)",help)
print(tuples)
for tuple in tuples:
    the[tuple[0]] = coerce(tuple[1])
    print(tuple[0],tuple[1])
print(the)
# the={}
# help:gsub("\n [-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)", 
#     function(k,x) the[k]=coerce(x) end)