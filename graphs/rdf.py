import numpy as np
from matplotlib import pyplot as plt

x,y= np.loadtxt('../analysis_303.15K/rdf.dat',unpack = True,usecols=(0,1),skiprows=(1))
x1,y1= np.loadtxt('../analysis_303.15K/rdf2.dat',unpack = True,usecols=(0,1),skiprows=(1))
x2,y2=np.loadtxt('../analysis_303.15K/rdf3.dat',unpack = True,usecols=(0,1),skiprows=(1))
x3,y3= np.loadtxt('../analysis_303.15K/rdf-inactive-1.dat',unpack = True,usecols=(0,1),skiprows=(1))
x4,y4= np.loadtxt('../analysis_303.15K/rdf-inactive-2.dat',unpack = True,usecols=(0,1),skiprows=(1))


plt.title("g(r) of MOR Receptors")
plt.xlabel("Distance (Å)")
plt.ylabel("g(r)")
plt.plot(x,y,color='red',label='active-150-200th ns')
#plt.plot(x1,y1,color='gold',label='active-350-400th ns')
plt.plot(x2,y2,color='green',label='active-500-568th ns')
plt.plot(x3,y3,color='navy',label='inactive-140-200th ns')
plt.plot(x4,y4,color='violet',label='inactive-260-320thns')
#plt.xlim(0)
#plt.ylim(0)
plt.legend()
plt.show()

