import numpy as np
from matplotlib import pyplot as plt

x,y = np.loadtxt('../analysis/morp_lig_rmsd.dat',unpack = True,usecols=(0,1),skiprows=(1))
a,b = np.loadtxt('../analysis/morp_lig_rmsd.dat',unpack = True,usecols=(0,2),skiprows=(51))
x1,y1 = np.loadtxt('../analysis2/morp_lig_rmsd.dat',unpack = True,usecols=(0,1),skiprows=(1))
a1,b1 = np.loadtxt('../analysis2/morp_lig_rmsd.dat',unpack = True,usecols=(0,2),skiprows=(51))
x2,y2 = np.loadtxt('../analysis3/morp_lig_rmsd.dat',unpack = True,usecols=(0,1),skiprows=(1))
a2,b2 = np.loadtxt('../analysis3/morp_lig_rmsd.dat',unpack = True,usecols=(0,2),skiprows=(51))

plt.title("RMSD of Ligand in Morphine-ActiveMOR Complex")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (Å)")
plt.plot(x,y,color='navy',alpha=0.9,label='replicate 1')
plt.plot(a,b,color='cornflowerblue')
plt.plot(x1,y1,color='orange',alpha=0.9,label='replicate 2')
plt.plot(a1,b1,color='navajowhite')
plt.plot(x2,y2,color='brown',alpha=0.9,label='replicate 3')
plt.plot(a2,b2,color='lightcoral')

plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()

