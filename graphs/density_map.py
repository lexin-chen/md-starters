import numpy as np
from matplotlib import pyplot as plt

#x,y = np.loadtxt('/orange/colina/le.chen/OpoidReceptor/BoxSizeAnalysis/Cube/ActiveMOR_107A_310K_150mM/Analysis/Conformations/sasavmd.dat',unpack = True,usecols=(0,1))
#x1,y1= np.loadtxt('../fentanyl_107A_310K_150mM/Analysis/sasavmd.dat',unpack = True,usecols=(0,1))

x,y,y1,y2,y3,y4=np.loadtxt('../analysis_303.15K/density_map_inactive.dat',unpack = True,usecols=(0,1,3,5,7,9),skiprows=(1))
x1,y5,y6,y7,y8,y9= np.loadtxt('../analysis_303.15K/density_map.dat',unpack = True,usecols=(0,1,3,5,7,9),skiprows=(1))
#y2=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(5),skiprows=(1))
#y3=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(7),skiprows=(1))

plt.title("Density Profile of MOR Receptors")
plt.xlabel("Z-coordinate")
plt.ylabel("Density (molecules/Å^3)")

#plt.plot(x,y,color='black',label='waters')
plt.plot(x,y1,color='red',label='POPC-inactive')
plt.plot(x,y2,color='gold',label='NPxxY-inactive')
plt.plot(x,y3,color='forestgreen',label='TM6-inactive')
plt.plot(x,y4,color='navy',label='inactive-protein')

#plt.plot(x1,y5,color='dimgray',linestyle='dashed',label='waters')
plt.plot(x1,y6,color='orange',linestyle='dashed',label='POPC-active')
plt.plot(x1,y7,color='yellow',linestyle='dashed',label='NPxxY-active')
plt.plot(x1,y8,color='green',linestyle='dashed',label='TM6-active')
plt.plot(x1,y9,color='royalblue',linestyle='dashed',label='protein-active')
#plt.ylim([0,10])
#plt.xlim(0)
plt.legend()
plt.show()

