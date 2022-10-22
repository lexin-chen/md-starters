#need to ml python/3.6 to get heatmap to work
import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
sns.set()

x,y,z= np.loadtxt('../analysis_restart/closestmols.dat',unpack = True,usecols=(0,1,2),skiprows=(1))
#x1,y1= np.loadtxt('../analysis_restart/closestmols-inactive.dat',unpack = True,usecols=(0,2),skiprows=(1))
a= x * 0.01
#a1= x1 * 0.1
#plt.title("Distance of the Closest Sodium Ion to D114")
#plt.xlabel("Time (ns)")
#plt.ylabel("Distance (Å)")
#plt.plot(a,y,color='orange',label='Active MOR')
#plt.plot(a1,y1,color='navy',label='Inactive MOR')

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

