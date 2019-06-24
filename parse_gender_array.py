import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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


aucs = [len(r) for r in final]
gss = [[], [], [], [], [], [], [], [], [], []]
counts = np.zeros(9)

for auc, gs in zip(aucs, final):
  if auc < 10:
    gss[auc] = gss[auc] + gs
    counts[auc-1] = counts[auc-1] + len(gs)

ratios = [np.mean(np.array(g)) for g in gss]

fig, w = plt.subplots()
w.plot(range(10), ratios, 'r-x') #x,y
# w.plot(range(10), -np.array(ratios) + 1) #x,y

w.set(xlabel='Number of authors per Paper', ylabel='Ratio of female names',
       title='Correlation Between Gender and Collaborations', ylim=[0, 0.3])
w.grid()

v = w.twinx()

v.stem(np.array(range(9)) + 1, counts, color='red', basefmt='')
v.set(ylabel='Author count', yscale='log')

plt.tight_layout()
fig.savefig("plot.pdf")
fig.savefig("plot.png")
# plt.show()

# IPython.embed()
