import numpy as np
import matplotlib.pyplot as plt

# Ce script etabli un modele polynomial quadratique y = a + bx + cx**2
# Par la suite il genere des observations aleatoires selon ce modele
# On resoud un probleme d'optimisation pour le resoudre


# Parametres pour l'affichage du trace
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.autolayout'] = True
plt.rcParams['font.size'] = 12

print("On definit le modele y = a + b*x + c*x**2")
print("-> donnez les coefficients a,b et c separes par un espace")
Coeff =  np.array(input(f'Coefficients du modeles\n').split(),dtype='float')
npts = int(input("Nombres d'observations\n"))
bruit = float(input("Niveau de bruit\n"))

def modele(coeff,x_val):
    return coeff[0] + coeff[1] * x_val + coeff[2] * x_val**2

def calc_obs_bruit(coeff,npts=50,bruit=0.0):
    # modele  y = a + bx + cx**2
    # Les observation sont generee aleatoirement entre -1 et 1
    Gen = np.random.default_rng()
    x_pts = Gen.uniform(low=-1.0,high=1.0,size=npts)
    # Du bruit est ajoute
    y_bruit = bruit * Gen.uniform(low=-1.0,high=1.0,size=npts)
    y_mod = modele(coeff,x_pts)
    y_obs = y_mod + y_bruit
    return x_pts,y_obs

def solve_optim(X_obs,Y_obs):
    # on cherche les constantes (a,b,c) du modele
    # a partir des observation
    matA = np.vstack((np.ones_like(X_obs),X_obs,X_obs**2)).T
    sol,res,rank,_ = np.linalg.lstsq(matA,Y_obs,rcond=None)
    print('Residus:',res[0])
    print('Rang de la matrice:',rank)
    return sol

X_true = np.linspace(-1,1,100)
Y_true = modele(Coeff,X_true)

X_obs, Y_obs = calc_obs_bruit(Coeff,npts=npts,bruit=bruit)
coeff_est = solve_optim(X_obs,Y_obs)
print('Coefficients exact:',Coeff)
print('Coefficients estimes:',coeff_est)
Y_est = modele(coeff_est,X_true)

plt.plot(X_obs,Y_obs,'o',color='black',label='observation')
plt.plot(X_true,Y_true,label='modele exact')
plt.plot(X_true,Y_est,label='modele calcule',linestyle='--')

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('probleme_quad.pdf')
plt.show()
