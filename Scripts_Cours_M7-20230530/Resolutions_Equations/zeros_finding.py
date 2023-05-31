import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect,newton

# Ce script défini 4 fonctions et recherche les zeros par différentes méthodes
# de NumPy

# Parametres pour l'affichage du trace
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 12

def fun1(x):
    return x**2 -x -1

def fun2(x):
    return x**3 - 3 * np.sin(x)

def fun3(x):
    return np.exp(x) - 2
def fprime3(x):
    return np.exp(x)

def fun4(x):
    return 1 - x**2 + np.sin(50/(1+x**2))

x_vec = np.linspace(-2,2,1000)

fun_labels = ['$f(x) = x^2-x-1$','$f(x) = x^3-3\,\sin{(x)}$','$f(x) = exp(x)-2$','$f(x) = \sin{(50/(1+x^2))}+1-x^2$']
funs = [fun1,fun2,fun3,fun4]

fig,axs = plt.subplots(nrows=2,ncols=2,sharex=True,sharey=False,figsize=(12,7))
i = 0
for fun,label_text in zip(funs,fun_labels):
    col = i%2
    row = i//2
    axs[col,row].plot(x_vec,fun(x_vec),linewidth=3.0)
    axs[row,col].set_ylabel('y')
    axs[row,col].grid()
    axs[row,col].set_title(label_text)
    axs[row,col].set_xlabel('x')
    axs[row,col].axhline(0,linestyle='--',linewidth=1.5,color='red')
    i+=1
plt.savefig('zeros_loc.pdf')
plt.show()

def dichotomie(fun,a,b,tol=1.0e-3):

    # Representation graphique (inutile)
    x_vec = np.linspace(a,b,1000)
    plt.figure(figsize=(8,3))
    plt.plot(x_vec,fun(x_vec))
    plt.plot([a,b],[fun(a),fun(b)],'o',color='black')
    plt.axhline(0,linestyle='--',linewidth=1.5,color='grey')
    # Representation graphique (inutile)
    
    dist = (b-a)
    i = 0
    while dist > tol:
        m = (a+b)*0.5
        fm = fun(m)
        i+=1
        plt.plot(m,fm,'+',color='red',ms=15,markeredgewidth=2.0)
        plt.text(m,fm-0.5,rf'$m_{i:d}$')
        if fm*fun(a) < 0:
            b = m
        elif fm*fun(b) < 0:
            a = m
        dist = (b-a)

    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('dichotomie_demo.pdf')
    plt.show()

    return m
    

def my_newton(fun,fprime,x0,tol=1.0e-3):

    # Representation graphique (inutile)
    x_vec = np.linspace(-2,2,1000)
    plt.figure(figsize=(8,3))
    plt.plot(x_vec,fun(x_vec))
    plt.plot(x0,fun(x0),'o',color='black')
    plt.axhline(0,linestyle='--',linewidth=1.5,color='grey')
    # Representation graphique (inutile)
    
    xk = x0
    fk = fun(x0)
    i = 0
    while np.abs(fk)>tol:
        i+=1
        fpk = fprime(xk)
        xk_new = xk - fk/fpk
        fk_new = fun(xk_new)
        plt.plot([xk,xk_new],[fk,0],color='purple',linewidth=1.0)
        fk_new = fun(xk_new)
        plt.plot(xk_new,fk_new,'+',color='red',ms=15,markeredgewidth=2.0)
        plt.text(xk_new,fk_new-0.5,rf'$x_{i:d}$')
        xk = xk_new
        fk = fk_new

    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('newton_demo.pdf')
    plt.show()

    return xk
    
    
sol3_mano = dichotomie(fun3,-2,2,tol=1.0e-2)
sol3_scipy = bisect(fun3,-2,2,xtol=1.0e-2)

print(rf'Methode de dichotomie avec la fonction {fun_labels[2]}')
print(f'A la main: {sol3_mano}')
print(f'Avec scipy: {sol3_scipy}')


sol3_mano = my_newton(fun3,fprime3,1.5,tol=1.0e-2)
sol3_scipy = newton(fun3,1.5,fprime=fprime3,rtol=1.0e-2)

print(rf'Methode de Newton avec la fonction {fun_labels[2]}')
print(f'A la main: {sol3_mano}')
print(f'Avec scipy: {sol3_scipy}')

