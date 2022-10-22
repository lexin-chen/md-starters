import numpy as np
from matplotlib import pyplot as plt

x,y,z= np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,2,3),skiprows=(1))
x1,y1,z1= np.loadtxt('../analysis2/distance.dat',unpack = True,usecols=(0,2,3),skiprows=(1))
x2,y2,z2= np.loadtxt('../analysis_qm/distance.dat',unpack = True,usecols=(0,2,3),skiprows=(1))
x3,y3,z3= np.loadtxt('../analysis_qm2/distance.dat',unpack = True,usecols=(0,2,3),skiprows=(1))

plt.title("Distance between Two Interactions in Active MOR")
plt.xlabel("Distance of R165-Y252 (Å)")
plt.ylabel("Distance of R165-T279 (Å)")
plt.scatter(y,z,color='red',label='CGenFF/2.5 & Membrane')
plt.scatter(y1,z1,color='gold',label='CGenFF/2.5 replicate & Membrane')
plt.scatter(y2,z2,color='blue',label='QM Parameters & Membrane')
plt.scatter(y3,z3,color='violet',label='QM Parameters replicate & Membrane')

#plt.colorbar()
plt.xlim(0,12)
plt.ylim(0,16)
plt.legend()
plt.show()

