import sympy as sp

point = [
    (2, 1),
    (3, -1),
    (-1, 2),
    (4, 3)
]

# Définir la variable symbolique
# x = sp.symbols('x')
#[] alpha
#[] f[]
x = [i[0] for i in point]
y = [i[1] for i in point]
# print(x,y)

class Resultat:
    def __init__(self, function, coefs, y0):
        self.function = function
        self.coef = coefs
        self.value = y0



def newton_coefficients(x, y):
    """
    Calcule les coefficients du polynôme de Newton
    à partir des points (x, y)
    """
    n = len(x)
    coef = y[:]  # copie de y
    # tableau des différences divisées
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def newton_eval(coef, x_data, x):
    """
    Évalue le polynôme de Newton en un point x
    coef : coefficients calculés avec newton_coefficients
    x_data : abscisses
    """
    if x is None:
        return "Veuillez renseigner un x0"
    n = len(coef)
    result = coef[-1]
    for i in range(n-2, -1, -1):
        result = result * (x - x_data[i]) + coef[i]
    return result

#Cette fonction va retourner l'expression brute(forme non factorisé) de la fonction de newton trouvé
def newton_function(x, coef):
    """
    Retrouve le polynome de newton
    coef : coefficients calculés avec newton_coefficients
    """
    n = len(coef)
    f = '1'
    for i in range(n):
        # signe devant le coefficient
        signe = " + " if coef[i] > 0 else " - "
        # valeur du coefficient (ignore 1)
        val = "" if abs(coef[i]) == 1 else str(abs(coef[i]))
        # produit (x - xj) pour j != i
        produit = ""
        for j in range(i):
            produit += f"(x {'-' if abs(x[j]>0) else '+'} {abs(x[j])})"
        f += f"{signe}{val}{produit}"
    return f

def newton(x, y, x0=None):
    """
    Retourne la fonction sous forme objet.
    Elle expose l'expression du polynome,
    le coefficient et la valeur de l'évaluation en un x0
    :param x:
    :param y:
    :param x0:
    :return:
    """
    coefs = newton_coefficients(x, y)
    return Resultat(
        coefs,
        newton_function(x, coefs),
        newton_eval(coefs, x, x0)
    )



# print(newton(x,y).value)