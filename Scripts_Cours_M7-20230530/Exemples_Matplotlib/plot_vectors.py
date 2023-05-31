import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 14

x = np.linspace(-np.pi,np.pi,50)
y = np.linspace(-np.pi,np.pi,50)
X,Y = np.meshgrid(x,y)

VX = np.sin(2*X)
VY = 0.01*Y**2
Vmag = np.sqrt(VX**2+VY**2)

plt.quiver(X,Y,VX,VY,Vmag,scale=10)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('vectors.png')
plt.savefig('vectors.pdf')
plt.show()