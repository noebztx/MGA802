import numpy as np
import matplotlib.pyplot as plt

# Ce script calcule les équation de deux droites qui passent chacune par 2 points
# Puis il calcule l'intersection des deux droites.

# Si False, la liste des points est fournie par le script et l'intersection est calculee
# Si Vrai, la liste des points est demandee a l'utilisateur et le calcul de l'intersection est aleatoire
interactive = True 
option = 'good' # choix 'good' ou 'bad' pour le conditionnement (utilise seulement en interactive = False)


# Parametres pour l'affichage du trace
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 12


def calc_a_b_droite(Pt1,Pt2):
    # Pt1 est un point defini par une paire (x1,y1)
    # Pt2 est un point defini par une paire (x2,y2)
    # On cherche a et b qui definisse la droite a x + b = y 
    # Qui passe par Pt1 et Pt2
    matA = np.array([[Pt1[0],1],[Pt2[0],1]])
    vecb = np.array([Pt1[1],Pt2[1]])
    sol = np.linalg.solve(matA,vecb)
    return sol[0],sol[1]
    
def calc_intersection_droites(D1,D2):
    # D1 est la droite 1 définie par une paire de coefficients (a1,b1)
    # D2 est la droite 2 définie par une paire de coefficients (a2,b2)
    # On cherche l'intersection des droites (xi,yi)
    matA = np.array([[D1[0],-1],[D2[0],-1]])
    vecb = np.array([-D1[1],-D2[1]])
    print('Conditionnement: ',np.linalg.cond(matA))
    sol = np.linalg.solve(matA,vecb)
    return sol[0],sol[1]


# Nous definissons 2 droites par 2 points chacunes
# Pts est un tableaux avec les coordonnees des 4 points
Pts = np.empty((4,2))

if interactive:
    option = 'user'
    print("On definit deux droites dont on va calculer l'intersection")
    # Les chaine de caracteres sont converties en specifiant le dtype
    for i in range(4):
        if i==0:
            print("La droite 1 passe par le point 1 et 2")
            print("-> donnez les coordonees x et y separees par un espace")
        if i==2:
            print("La droite 2 passe par le point 3 et 4")
        Pts[i,:] =  np.array(input(f'Coordonnees (x,y) du point {i+1}\n').split(),dtype='float') 

else:
    if option == 'good':
        # Bien definie
        Pts = np.array([[ 1.2,  4.2],
                        [-1. ,  1. ],
                        [-2.5,  7.1],
                        [ 3. , -2. ]])
    elif option == 'bad':
        # Moins bien definie
        Pts = np.array([[ 1.2,  4.2],
                        [-1. ,  1. ],
                        [-2.5,  -0.6],
                        [ 3. , 6.3 ]])
    

x = np.linspace(Pts[:,0].min(),Pts[:,0].max())
a1,b1 = calc_a_b_droite(Pts[0],Pts[1])
a2,b2 = calc_a_b_droite(Pts[2],Pts[3])


plt.plot(Pts[:,0],Pts[:,1],'o',color='black',label='points')
plt.plot(x,a1*x+b1,label='droite 1',color='green')
plt.plot(x,a2*x+b2,label='droite 2',color='orange')
plt.plot()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

if interactive:
    reponse = input("Voulez vous calculez l'intersection des droites? [oui/non]\n")
    if reponse == 'yes':
        calc_intersection = True
    else:
        calc_intersection = False
else:
    calc_intersection = True

if calc_intersection:

    xi,yi = calc_intersection_droites([a1,b1],[a2,b2])

    plt.plot(Pts[:,0],Pts[:,1],'o',color='black',label='points')
    plt.plot(x,a1*x+b1,label='droite 1',color='green')
    plt.plot(x,a2*x+b2,label='droite 2',color='orange')
    plt.plot(xi,yi,'+',ms=15,color='red',markeredgewidth=3.0)
    plt.plot()
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.savefig(f'intersec_droite_{option}.pdf')
    plt.show()

