import numpy as np
import argparse
from collections import deque, defaultdict
parser = argparse.ArgumentParser()
parser.add_argument('--model', dest='mdf')
parser.add_argument('--prefix', dest='pref', default="")
parser.add_argument('--length', dest='clg')
args=parser.parse_args()
mdf = args.mdf
pref = args.pref
pref = pref.replace(',', ' ')
pref = pref.split()
clg = args.clg
n=3
ban = """ #№$%^/|&*_=+""" # no -
dot = """"'[{]}\\<>.!?;:"""
mstr = ban[1]
mstr2 = ban[3]
trigcnt = defaultdict(lambda: ['.'])
b = open(mdf)
for x in b:
    x = x.strip()
    cs = x.split(mstr2)
    trigcnt[tuple(cs[:-1]) ].append(cs[2])
b.close()
cans = pref
while len(pref) < n-1:
    pref.append(3)
    
