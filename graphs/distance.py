import numpy as np
from matplotlib import pyplot as plt

x,y = np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1 = np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,2),skiprows=(1))
x2,y2 = np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,3),skiprows=(1))
x3,y3 = np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,4),skiprows=(1))

plt.title("Distance of Key Interactions in the Active MOR")
plt.xlabel("Time (ns)")
plt.ylabel("Distance (Å)")

plt.plot(x,y,color='red',label='Manually Placed Na+ to D114')
plt.plot(x1,y1,color='yellow',label='D147-Nitrogen in ligand')
plt.plot(x2,y2,color='blue',label='H297-Phenol in Ligand')
plt.plot(x3,y3,color='violet',label='Disulfide bond')
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()









