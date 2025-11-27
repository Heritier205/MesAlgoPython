# Dans ce programme nous prendrons x²-2=0 comme exemple d'equation a resoudre
import math
from functions import G as f
cpt = 0
n = 0
tries = 0
h = 0.1




def dichotomie(inf, sup, pas):
    global cpt, tries
    if tries == 0 :
        print("-------Methode de dichotomie-------- ")
    tries += 1
    cpt = 0
    if f(inf)*f(sup)<0 :
        while (sup-inf)>pas and f(inf)*f(sup)<0:
            cpt+=1
            if f(inf)*f((sup+inf)/2) <0 :
                sup = (sup+inf)/2
            else : inf = (inf+sup)/2
        return (f"La solution est comprise entre  --- [ {inf} ; {sup} ] "
                f"---\nTrouvé apres {cpt} itteration{'s'if cpt>1 else ''}")
    else :
        balayage(inf, sup)
        return f"{"La solution n'est pas cette intervalle !!\n" if n == 0 else ''}"

def balayage(inf,sup) :
    global n
    inf0, sup0 = inf, inf+h
    while sup - inf0 > h :
        while f(sup0) * f(inf0) > 0 and sup0 < sup:
            inf0, sup0 = sup0, sup0 + h
        if f(sup0) * f(inf0) < 0:
            print(f"\nune solution x{n} se situe dans l'intervalle   "
                  f"--[{inf0:.2f} ; {sup0:.2f}]--\n{dichotomie(inf0, sup0, 1e-10)}")
            n += 1
        elif f(sup0) * f(inf0) == 0:
            if f(sup0)==0:
                print(f"une solution x{n} se trouve aux bornes : x{n} = {sup0}")
            else:
                print(f"une solution x{n} se trouve aux bornes : x{n} = {inf0}")
            n += 1
        inf0 = sup0

# balayage(-1, 1)
