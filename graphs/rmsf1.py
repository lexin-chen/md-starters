import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis/rmsf.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis/rmsf.dat',unpack = True,usecols=(0,2),skiprows=(1))
x2,y2= np.loadtxt('../analysis/rmsf.dat',unpack = True,usecols=(0,3),skiprows=(1))

a = x + 51 #change to 65 

plt.title("RMSF of Active MOR Receptors-CGenFF/2.5 Parameters")
plt.xlabel("Residues")
plt.ylabel("RMSF (Å)")
plt.plot(a,y,color='red',label='all frames past equilibration') #linewidth=width alpha=transparency
plt.plot(a,y1,color='gold',label='last 100ns')
plt.plot(a,y2,color='navy',label='last 50ns')
plt.xlim(52,347)
plt.ylim(0)
plt.legend()
plt.show()

