import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis_qm/totalpairs.dat',unpack = True,usecols=(1,2),skiprows=(1))
x1,y1 = np.loadtxt('../analysis_qm2/totalpairs.dat',unpack = True,usecols=(1,2),skiprows=(1))
x2,y2 = np.loadtxt('../analysis/totalpairs.dat',unpack = True,usecols=(1,2),skiprows=(1))
a=x+51
b=x1+51
c=x2+51

ax = plt.subplot(111)
plt.title("Contacts for Active MOR Ligands")
ax.bar(a-0.2, y, width=0.2, color='b', align='center',label='QM')
ax.bar(b, y1, width=0.2, color='g', align='center',label='QM replicate')
ax.bar(c+0.2, y2, width=0.2, color='r', align='center',label='cgenff/2.5')
plt.legend()

#plt.bar(a,y)
#plt.title("Docking Results for Active MOR Ligands")
#plt.xlabel("Ligands")
#plt.ylabel("Docking Score (kcal/mol)")
#plt.ylim(0)
plt.show()

