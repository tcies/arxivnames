import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
input = [[1,1,0,1],[0,1,1,1],[0,1,1,1], [0,1,1,1], [0,1,1,1], [0,1,0,1]]
for x in input:
	print len(x)


t = np.arange(0, 6)
s = [[1,1,0,1],[0,1,1,1],[0,1,1,1], [0,1,1,1], [0,1,1,1], [0,1,0,1]]
# p = np.arange(0, 6)

fig, w = plt.subplots()
w.plot(t, s) #x,y



w.set(xlabel='Number of authors per Paper', ylabel='Ratio',
       title='Correlation Between Gender and Collaborations')
w.grid()

fig.savefig("plot.png")
plt.show()
