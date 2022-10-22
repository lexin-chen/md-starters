import numpy as np
from matplotlib import pyplot as plt

x,y = np.loadtxt('../analysis/dihedral.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1 = np.loadtxt('../analysis/dihedral.dat',unpack = True,usecols=(0,2),skiprows=(1))

plt.title("Dihedral of W293 in Active MOR")
plt.xlabel("Time (ns)")
plt.ylabel("Dihedral Angle (°)")

plt.plot(x,y,color='orange',label='W293 Chi1')
plt.plot(x1,y1,color='navy',label='W293 Chi2')
plt.xlim(0)
plt.ylim(-200,200)
plt.legend()
plt.show()

