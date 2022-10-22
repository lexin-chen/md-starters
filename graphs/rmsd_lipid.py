import numpy as np

from matplotlib import pyplot as plt

x,y= np.loadtxt('../../box_size_analysis/lig_npat_90_10/analysis/rmsd_303.15.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../../box_size_analysis/lig_npat_80_20/analysis/rmsd.dat',unpack = True,usecols=(0,1),skiprows=(1))
plt.title("RMSD of Transmembrane residues of Different Lipid Compositions")
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (Å)")
plt.plot(x,y,color='orange',label='9:1 POPC:CHL')
plt.plot(x1,y1,color='blue',label='8:2 POPC:CHL')
#plt.plot(x1,y1,color='navy',label='310K')

plt.xlim(0)
#plt.ylim(0)
plt.legend()
plt.show()

