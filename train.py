import numpy as np
import argparse
from collections import deque, defaultdict
parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', dest='idir')
parser.add_argument('--model', dest='mdf')
args=parser.parse_args()
idir = args.idir
mdf = args.mdf
a = open(idir)
n=3
dq = deque()
trigcnt = []
ban = """ #№$%^/|&*_=+""" # no -
dot = """"'[{]}\\<>.!?;:"""
for x in a:
    x = list(x.strip().lower())
    for i in range(len(x)):
        if x[i] in ban:
            x[i] = ' '
        elif x[i] in dot:
            x[i] = '.'
    t = []
    for c in x:
        if (c == ' ' or c == '.') and t:
            dq.append(''.join(t))
        if c == '.':
            t = ['.']
        elif c == ' ':
            t = []
        else:
            t.append(c)
    if t:
        dq.append(''.join(t))
    while len(dq) >= n:
        trigcnt.append(tuple(dq[i] for i in range(n)))
        dq.popleft()
b = open(mdf, mode='w')
mstr = ban[1]
mstr2 = ban[3]
b.write('\n'.join(mstr2.join(x) for x in trigcnt))
b.close()
