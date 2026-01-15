def poly_mul(p1, p2):
    """Multiplie deux polynômes représentés par des listes de coefficients"""
    deg = len(p1) + len(p2) - 1
    result = [0.0] * deg
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result

def poly_add(p1, p2):
    """Additionne deux polynômes représentés par des listes de coefficients"""
    # Ajuster la taille
    if len(p1) < len(p2):
        p1 = [0]*(len(p2)-len(p1)) + p1
    elif len(p2) < len(p1):
        p2 = [0]*(len(p1)-len(p2)) + p2
    return [p1[i] + p2[i] for i in range(len(p1))]

def poly_eval(p, x):
    """Évalue le polynôme p en x"""
    val = 0
    deg = len(p)
    for i in range(deg):
        val += p[i] * (x**(deg-1-i))
    return val

def lagrange_interpolation():
    # Saisie des points
    n = int(input("Nombre de points : "))
    x_vals = []
    y_vals = []
    for i in range(n):
        x = float(input(f"x[{i}] = "))
        y = float(input(f"y[{i}] = "))
        x_vals.append(x)
        y_vals.append(y)
    
    x_point = float(input("Valeur de x à interpoler : "))

    # Polynôme final (liste de coefficients)
    P = [0.0]

    for i in range(n):
        # L_i(x) = 1
        Li = [1.0]
        denom = 1.0
        for j in range(n):
            if i != j:
                # Multiplier par (x - x_j)
                Li = poly_mul(Li, [1.0, -x_vals[j]])
                denom *= (x_vals[i] - x_vals[j])
        # Multiplier par y_i / denom
        Li = [c * (y_vals[i]/denom) for c in Li]
        # Ajouter au polynôme final
        P = poly_add(P, Li)

    # Affichage du polynôme
    poly_str = ""
    deg = len(P)
    for i, coef in enumerate(P):
        if abs(coef) > 1e-12:
            if poly_str != "":
                poly_str += " + "
            poly_str += f"{coef:.3f}*x^{deg-1-i}"
    print("\nPolynôme de Lagrange développé :")
    print("P(x) =", poly_str)

    # Calcul valeur interpolée
    P_val = poly_eval(P, x_point)
    print(f"\nValeur interpolée en x = {x_point} : {P_val:.6f}")

# Boucle principale pour recommencer
while True:
    lagrange_interpolation()
    choix = input("\nVoulez-vous recommencer ? (o/n) : ").strip().lower()
    if choix != 'o':
        print("Fin du programme.")
        break
