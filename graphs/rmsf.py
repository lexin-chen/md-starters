import numpy as np
from matplotlib import pyplot as plt

x3,y3=np.loadtxt('../../morp_107A_310K_150mM/Analysis/rmsf.dat',unpack = True,usecols=(0,1),skiprows=(1))
x,y= np.loadtxt('../analysis/rmsf.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis_legacy/rmsf.dat',unpack = True,usecols=(0,1),skiprows=(1))
x2,y2= np.loadtxt('../analysis_qm/rmsf.dat',unpack = True,usecols=(0,1),skiprows=(1))

a = x + 51 #change to 65 

plt.title("RMSF of Active MOR Receptors")
plt.xlabel("Residues")
plt.ylabel("RMSF (Å)")
plt.plot(a,y3,color='red',label='CGenFF/2.5+310K')
plt.plot(a,y,color='orange',label='CGenFF/2.5') #linewidth=width alpha=transparency
plt.plot(a,y1,color='blue',label='CGenFF/1.0.0 (Legacy)')
plt.plot(a,y2,color='black',label='QM Paper')
plt.xlim(52,347)
plt.ylim(0)
plt.legend()
plt.show()

