# import re

# help = """
# CSV : summarized csv file
# (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
# USAGE: lua seen.lua [OPTIONS]

# OPTIONS:
# -e --eg start-up example = nothing
# -d --dump on test failure, exit with stack dump = false
# -f --file file with csv data = ../data/auto93.csv
# -h --help show help = false
# -n --nums number of nums to keep = 512
# -s --seed random number seed = 10019
# -S --seperator feild seperator = ,"""

# def coerce(s):
#     def fun(s1):
#         if s1=='true':
#             return True 
#         if s1=='false':
#             return False  
#         return s1

#     if s.isnumeric():
#         return int(s)
#     else:
#         a = fun(re.search("\s(.-)\s$",s))
#         print(a)
#         return a
#     #return int(s) or fun(re.search("^\s*(.-)\s*$",s)) #edit the parameter of fun

# the = {}
# tuples = re.findall("[-][\S][\s][-][-]([\S]+)[^\n]+= ([\S]+)",help)
# for tuple in tuples:
#     the[tuple[0]] = coerce(tuple[1])
# print(the)
