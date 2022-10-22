import numpy as np
from matplotlib import pyplot as plt

x,y = np.loadtxt('../analysis/rmsd.dat',unpack = True,usecols=(0,1),skiprows=(1))

plt.title("RMSD of transmembrane region of receptor in Morphine-ActiveMOR Complex")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (Å)")
plt.plot(x,y,color='navy',label='')
plt.xlim(0)
plt.ylim(0,3)
#plt.legend()
plt.show()

