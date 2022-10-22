import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis_303.15K/rg.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis_310K/rg.dat',unpack = True,usecols=(0,1),skiprows=(1))

plt.title("Rg of Active MOR Receptors")
plt.xlabel("Time (ns)")
plt.ylabel("Rg (Å)")
plt.plot(x,y,color='orange',label='303.15K')
plt.plot(x1,y1,color='navy',label='310K')

plt.xlim(0)
#plt.ylim(0)
plt.legend()
plt.show()

