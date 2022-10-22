import numpy as np
from matplotlib import pyplot as plt

#x,y = np.loadtxt('/orange/colina/le.chen/OpoidReceptor/BoxSizeAnalysis/Cube/ActiveMOR_107A_310K_150mM/Analysis/Conformations/sasavmd.dat',unpack = True,usecols=(0,1))
#x1,y1= np.loadtxt('../fentanyl_107A_310K_150mM/Analysis/sasavmd.dat',unpack = True,usecols=(0,1))

x,y,y1,y2,y3,y4,y5,y6,y7,y8=np.loadtxt('../analysis_303.15K/number_density_inactive.dat',unpack = True,usecols=(0,1,3,5,7,9,11,13,15,17),skiprows=(1))
#y1= np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(3),skiprows=(1))
#y2=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(5),skiprows=(1))
#y3=np.loadtxt('../analysis_303.15K/number_density.dat',unpack = True,usecols=(7),skiprows=(1))

plt.title("Density of Active MOR Receptors")
plt.xlabel("Time (ns)")
plt.ylabel("Density (Å^3)")
plt.plot(x,y,color='black',label='waters')
#plt.plot(x,y1,color='pink',label='protein')
plt.plot(x,y2,color='red',label='1')
plt.plot(x,y3,color='orange',label='2')
plt.plot(x,y4,color='yellow',label='3')
plt.plot(x,y5,color='green',label='4')
plt.plot(x,y6,color='blue',label='5')
plt.plot(x,y7,color='indigo',label='6')
plt.plot(x,y8,color='violet',label='7')
plt.ylim([0,10])
#plt.xlim(0)
plt.legend()
plt.show()

