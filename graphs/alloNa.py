import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis_restart/closestmols.dat',unpack = True,usecols=(0,2),skiprows=(1))
x1,y1= np.loadtxt('../analysis_restart/closestmols-inactive.dat',unpack = True,usecols=(0,2),skiprows=(1))
a= x * 0.1
a1= x1 * 0.1
plt.title("Distance of the Closest Sodium Ion to D114")
plt.xlabel("Time (ns)")
plt.ylabel("Distance (Å)")
plt.plot(a,y,color='orange',label='Active MOR')
plt.plot(a1,y1,color='navy',label='Inactive MOR')

plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()

