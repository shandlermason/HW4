# Handle settings
import math
import re
from contextlib import closing
import requests
import codecs
import csv


options = '''
CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD−2 license
USAGE: lua seen.lua [OPTIONS]

OPTIONS:
−e −−eg start−up example = nothing
−d −−dump on test failure, exit with stack dump = false
−f −−file file with csv data = ../data/auto93.csv
−h −−help show help = false
−n −−nums number of nums to keep = 512
−s −−seed random number seed = 10019
S −−seperator field seperator = ,]]

−− Function argument conventions:
−− 1. two blanks denote optionas, four blanls denote locals:
−− 2. prefix n,s,is,fun denotes number,string,bool,function;
−− 3. suffix s means list of thing (so names is list of strings)
−− 4. c is a column index (usually)
'''


def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def func(s1):
    if s1 == "true":
        return True
    elif s1 == "false":
        return False
    return s1


def coerce(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s.strip()


def cli():
    pass


# Lists 
def copy(t):
    """Deep Copy"""
    if type(t) == 'dict':
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


def csv1(fname, fun):
    """Call fun on each row. Row cells are divided in the.seperator"""
    sep = the["seperator"]
    src = open(fname)
    while True:
        s = src.readline()
        if not s:
            return src.close()
        else:
            t = {}
            for s1 in s.split(sep):
                t[1+len(t)] = coerce(s1)
            fun(t)
            
    
# Strings
def o(t):
    if type(t) != dict:
        return str(t)
    def show(k, v):
        match_str= re.compile("^_")
        if not re.findall(match_str, str(k)):
            v = o(v)
            return len(t)==0 and "{}".format(k,v) or str(v)
    u = dict()
    for k, v in t.items():
        u[1+len(u)] = show(k, v)
    if len(t)==0:
        sorted(u)
    return u

def oo(t):
    print(o(t))
    return t


# Miscs

def rouges():
    pass


# Maths
def rnd(x, places):
    mult = 10 ** places
    return math.floor(x * mult + 0.5) / mult


def csv_function(url):
    row_list1 = []
    url = url
    with closing(requests.get(url, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        for row in reader:
            for cell in row:
                temp = row.index(cell)
                temp1 = coerce(cell)
                row[temp] = temp1
            row_list1.append(row)
    return row_list1


the = {}
group1 = re.findall(r"[−][−]([\w]+)", options)  # word after the 2 dashes
group2 = re.findall(r"((?<= = ).*)", options)  # what is after equal sign
print(group1)
for k in group1:
    for x in group2:
        the[k] = coerce(x)
        group2.remove(x)
        break

    
    