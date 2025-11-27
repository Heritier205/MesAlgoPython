# Dans ce programme nous prendrons x²-2=0 comme exemple d'equation a resoudre
# x=(1/2)(x+2/x)
import math
from functions import pt_fixe_suite as g
from functions import show, maxtries, maxcpt
tol = 1e-10
cpt , tries= 0, 0

# Avec la recursivite
def point_fixe2(x, pas):
    global cpt
    if abs(g(x)-x) < pas :
        return x
    else:
        cpt+=1
        return point_fixe2(g(x),pas)

# Avec la boucle while
def point_fixe(x, pas):
    print("-------Methode de substitution ou point fixe-------- ")
    global cpt, tries
    while tries <= 10 :
        try :
            while abs(g(x)-x) > pas :
                cpt+=1
                x = g(x)
            if cpt == 0:
                return maxcpt(tries, cpt)
            return show(x,cpt,tries)
        except ZeroDivisionError :
            tries +=1
            eps = tol*(1+abs(x))
            x += eps
    return maxtries(tries)


# print(point_fixe(0,1e-10))