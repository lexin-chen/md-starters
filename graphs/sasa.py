import numpy as np
from matplotlib import pyplot as plt

#x,y = np.loadtxt('/orange/colina/le.chen/OpoidReceptor/BoxSizeAnalysis/Cube/ActiveMOR_107A_310K_150mM/Analysis/Conformations/sasavmd.dat',unpack = True,usecols=(0,1))
#x1,y1= np.loadtxt('../fentanyl_107A_310K_150mM/Analysis/sasavmd.dat',unpack = True,usecols=(0,1))

x,y= np.loadtxt('../analysis_303.15K/sasa.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis_restart/sasa.dat',unpack = True,usecols=(0,1),skiprows=(1))

plt.title("SASA of Active MOR Receptors at 303.15")
plt.xlabel("Time (ns)")
plt.ylabel("SASA (Å²)")
plt.plot(x,y,color='orange',label='with membrane')
plt.plot(x1,y1,color='navy',label='with membrane restart')
plt.xlim(0)
plt.legend()
plt.show()

