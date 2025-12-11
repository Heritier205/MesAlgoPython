#  la fonction
import math

def G(x):
    return math.log(abs(x))*5


#  la derive de la fonction
def g(x):
    return 5/x


def pt_fixe_suite(x):
    return (1/2)*(x+1/x)

def show(x,cpt,tries):
    return (f"La solution est X = {x} \nTrouvé apres {cpt} itteration{'s' if cpt>1 else ''} "
            f"{f"et {tries} stabilisation{'s'if tries > 1 else ''}" if tries else ''}")

def maxtries(tries):
    return (f"\n!! Les points fournis provoquent un calcul instable. , "
            f"\nSolution non trouve au bout de {tries} stabilisation{'s' if tries>1 else ''} !!\n"
            "----Veuillez utiliser d'autres points plus proche de la racine !! ")


def maxcpt(tries, cpt):
    return (f"\n!! Votre fonction ne converge pas , Solution non trouve au bout de {cpt-1} itteration{'s' if cpt > 1 else ''} {f"de la {tries}{'eme' if tries > 1 else 'ere'} stabilisation " if tries else '' } !!\n"
            "----Veuillez utiliser d'autres points plus proche de la racine !! ")
