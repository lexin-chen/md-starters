import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
#import matplotlib as plt
from matplotlib import pyplot as plt
sns.set()

#ix = np.arange(start=0, stop=12)
#y = np.arange(start=0, stop = 500)
#BP.nastruct.dat
x = np.loadtxt('../analysis_303.15K/density_map_inactive.dat',unpack = True,usecols=(1),skiprows=(1))
#x1=x/5
y = np.loadtxt('../analysis_303.15K/density_map_inactive.dat',unpack = True,usecols=(1),skiprows=(1))
z = np.loadtxt('BP.nastruct.dat',unpack = True,usecols=(12),skiprows=(1))

df = pd.DataFrame.from_dict(np.array([x1,y,z]).T)
df.columns = ['Time(ns)','Basepair number','Minor Groove']
df['Minor Groove'] = pd.to_numeric(df['Minor Groove'])
pivotted= df.pivot('Basepair number','Time(ns)','Minor Groove')
sns.heatmap(pivotted,cmap='RdBu')
plt.title("Width of Minor Groove in DNA (Angstroms)")
plt.show()

#x,y = np.loadtxt('/orange/colina/le.chen/OpoidReceptor/BoxSizeAnalysis/Cube/ActiveMOR_107A_310K_150mM/Analysis/Conformations/sasavmd.dat',unpack = True,usecols=(0,1))
#x1,y1= np.loadtxt('../fentanyl_107A_310K_150mM/Analysis/sasavmd.dat',unpack = True,usecols=(0,1))

x,y,y1,y5=np.loadtxt('../analysis_303.15K/density_map_inactive.dat',unpack = True,usecols=(0,1,3,5),skiprows=(1))
x1,y2,y3,y4= np.loadtxt('../analysis_303.15K/density_map.dat',unpack = True,usecols=(0,1,3,5),skiprows=(1))
#y2=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(5),skiprows=(1))
#y3=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(7),skiprows=(1))

plt.title("Density of Active MOR Receptors")
plt.xlabel("Z-coordinate")
plt.ylabel("Density (Å)")
plt.plot(x,y,color='black',label='NPxxY-inactive')
plt.plot(x,y1,color='pink',label='TM6-inactive')
plt.plot(x,y5,color='yellow',label='ianctive-protein')
plt.plot(x1,y2,color='blue',label='NPxxY-active')
plt.plot(x1,y3,color='indigo',label='TM6')
plt.plot(x1,y4,color='gold',label='protein-active')
#plt.ylim([0,10])
#plt.xlim(0)
plt.legend()
plt.show()

