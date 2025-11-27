# Dans ce programme nous prendrons x²-2=0 comme exemple d'equation a resoudre

import math
from functions import *
cpt, tries = 0, 0
tol = 1e-10
# la suite
def phi(x):
    try : Gx = G(x)
    except ZeroDivisionError: raise ZeroDivisionError
    except ValueError : raise ValueError
    except OverflowError: raise ValueError

    try : gx = g(x)
    except ZeroDivisionError: raise ZeroDivisionError
    except ValueError : raise ValueError
    except OverflowError: raise ValueError

    if gx < tol :
        raise  ZeroDivisionError

    xn = Gx/gx

    if math.isnan(xn) or math.isinf(xn) : raise OverflowError

    return x-(Gx/gx)


def newton(x,pas):
    print("-------Methode de Newton Raphson-------- ")
    global cpt, tries
    while tries < 10 :
        try :
            xn = phi(x)
            while abs(xn-x) > pas and cpt <= 100:
                cpt += 1
                x = xn
                xn = phi(x)
            if cpt > 100 :
                return maxcpt(tries,cpt)
            return show(x, cpt, tries)
        except (ZeroDivisionError, OverflowError):
            tries += 1
            print("Le point entré annule le denominateur de la suite Phi\n"
                  "Nous allons donc proceder a un changement du point b\n")
            eps = tol * (1 + abs(x))
            x += eps
            print(f"La nouvelle valeur prise est : x0 = {x}\n")
        except ValueError :
            tries += 1
            print("\nLe x0 entré ne respecte pas la fonction g(x)\n"
                  "Nous allons donc proceder a un changement du point x0\n")
            eps = tol * (1 + abs(x))
            x += eps
            print(f"La nouvelle valeur prise est : x0 = {x}")
    return maxtries(tries)


# print(newton(0,1e-10))