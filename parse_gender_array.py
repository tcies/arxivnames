import IPython
from IPython.core import ultratb
import sys


sys.excepthook = ultratb.FormattedTB(
color_scheme='Linux', call_pdb=1)

with open('author_gender.csv') as f:
    content = f.readlines()

content = content[1:]
gs = []
for line in content:
    n, g = line.rstrip().split(',')
    if g == 'male':
        gs.append(0)
    elif g == 'female':
        gs.append(1)
    else:
        gs.append(-1)

with open('indices.txt') as f:
    indices = f.readlines()
    
indices = [int(i) for i in indices]

result = dict()

assert len(indices) == len(gs)

for index, g in zip(indices, gs):
    if index in result:
        result[index].append(g)
    else:
        result[index] = [g]

reslist = [r[1] for r in result.iteritems()]
final = [r for r in reslist if -1 not in r]

IPython.embed()
