# Script pour realiser un trace simple

import numpy as np
import matplotlib.pyplot as plt


# quelques parametre pour le graphique
plt.rcParams['font.size'] = 14
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100


# donnees a tracer
x = np.linspace(0,10,500)
# Polynome d'ordre 2
y_2 = x**2-2*x+4
# Polynome d'ordre 3
y_3 = 0.1*x**3-1.2*x**2-0.5*x+15


# Bloc de code pour le trace
plt.plot(x,y_2,label='polynome 2nd ordre')
plt.plot(x,y_3,label='polynome 3e ordre',linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Mon premier graphique')
plt.savefig('ma_premiere_figure.png')
plt.savefig('ma_premiere_figure.pdf')
plt.show()