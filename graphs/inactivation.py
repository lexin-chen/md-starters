import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis2/distance.dat',unpack = True,usecols=(0,1),skiprows=(1))
x2,y2= np.loadtxt('../analysis_qm/distance.dat',unpack = True,usecols=(0,1),skiprows=(1))
x3,y3= np.loadtxt('../analysis_qm2/distance.dat',unpack = True,usecols=(0,1),skiprows=(1))

plt.title("Distance of Manually Placed Sodium Ion to D114 of Active MOR")
plt.xlabel("Time (ns)")
plt.ylabel("Distance (Å)")
plt.plot(x,y,color='red',label='CGenFF/2.5 & Membrane')
plt.plot(x1,y1,color='gold',label='CGenFF/2.5 replicate & Membrane')
plt.plot(x2,y2,color='blue',label='QM Parameters & Membrane')
plt.plot(x3,y3,color='violet',label='QM Parameters replicate & Membrane')

plt.xlim(0)
plt.ylim(0)
#plt.legend()
plt.show()

