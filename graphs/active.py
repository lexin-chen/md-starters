#need to ml python/3.6 to get heatmap to work
import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
sns.set()

x,y,z= np.loadtxt('../analysis/distance.dat',unpack = True,usecols=(0,1,2),skiprows=(1))
x1,y1,z1= np.loadtxt('../analysis2/distance.dat',unpack = True,usecols=(0,1,2),skiprows=(1))
x2,y2,z2= np.loadtxt('../analysis_qm/distance.dat',unpack = True,usecols=(0,1,2),skiprows=(1))
x3,y3,z3= np.loadtxt('../analysis_qm2/distance.dat',unpack = True,usecols=(0,1,2),skiprows=(1))

df = pd.DataFrame.from_dict(np.array([x,y,z]).T)
df.columns = ['Time (ns)','Atom #','Distance']
df['Distance'] = pd.to_numeric(df['Distance'])
pivotted= df.pivot('Atom #','Time (ns)','Distance')
sns.heatmap(pivotted,cmap='RdBu')
plt.title("Closest Sodium Ion to D114 in ActiveOR")
plt.show()

#plt.xlim(0)
#plt.ylim(0)
#plt.legend()
#plt.show()

plt.title("Distance of Manually Placed Sodium Ion to D114 of Active MOR")
plt.xlabel("Time (ns)")
plt.ylabel("Distance (Å)")
plt.scatter(y,b,c=x,marker='+',label='CGenFF/2.5 & Membrane')
plt.scatter(y1,b1,c=x1,marker='o',label='CGenFF/2.5 replicate & Membrane')
plt.scatter(y2,b2,c=y2,marker='x',label='QM Parameters & Membrane')
plt.scatter(y3,b3,c=y3,marker='s',label='QM Parameters replicate & Membrane')
#plt.colorbar()
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()

