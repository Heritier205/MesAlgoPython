# Dans ce programme nous prendrons x²-2=0 comme exemple d'equation a resoudre

import math
import random
from functions import G as g, maxtries, show, maxcpt

cpt = 0
tries = 0
tol = 1e-10


def phi(x0,x1):
    try : g0 = g(x0)
    except ZeroDivisionError : raise ZeroDivisionError
    except OverflowError : raise OverflowError
    except ValueError : raise ValueError


    try : g1 = g(x1)
    except ZeroDivisionError : raise ZeroDivisionError
    except OverflowError : raise OverflowError
    except ValueError : raise ValueError

    if abs(g1-g0) <= tol:
        raise ZeroDivisionError

    xn = (g1*x0 - g0*x1) / (g1-g0)

    if math.isnan(xn) or math.isinf(xn):
        raise OverflowError

    return xn







def secante(x0, x1, pas):
    print("-------Methode de la secante -------- ")
    global cpt, tries
    while tries <= 10 :
        try :
            xn = phi(x0,x1)
            while abs(xn-x0) > pas and cpt <= 100:
                cpt += 1
                x0, x1 = x1, xn
                xn = phi(x0,x1)
            if cpt > 100 :
                return maxcpt(tries,cpt)
            else : return show(xn, cpt, tries)
        except (ZeroDivisionError, OverflowError) :
            tries += 1
            print("\nLes points entrés annulent le denominateur de la Suite Phi\n"
                  "Nous allons donc proceder a un changement du point b\n")
            eps = tol * (1 + abs(x1))
            x1 += eps
            print(f"Les nouvelle valeurs prise sont : a = {x0} ; b = {x1}\n")
        except ValueError :
            tries += 1
            print("\nLes points entrés ne respectent pas la fonction g(x)\n"
                  "Nous allons donc proceder a un changement des point a et b\n")
            eps = tol * (1 + abs(x0))
            x0 += eps
            eps = tol * (1 + abs(x1))
            x1 += eps
            print(f"Les nouvelle valeurs prise sont : a = {x0} ; b = {x1}\n")
    return maxtries(tries)





# print(secante(100,0,1e-20))