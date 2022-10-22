import numpy as np

from matplotlib import pyplot as plt

x,y= np.loadtxt('../../box_size_analysis/lig_npat_90_10/analysis/minimagedist_303.15',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../../box_size_analysis/lig_npat_90_10/analysis/minimagedist_310',unpack = True,usecols=(0,1),skiprows=(1))
plt.title("Minimum image of Active MOR in Membrane Small Boxes")
plt.xlabel("Time (ns)")
plt.ylabel("Minimum Image Distance (Å)")
plt.plot(x,y,color='orange',label='303.15K')
plt.plot(x1,y1,color='blue',label='310K')
#plt.plot(x1,y1,color='navy',label='310K')

plt.xlim(0)
#plt.ylim(0)
plt.legend()
plt.show()

