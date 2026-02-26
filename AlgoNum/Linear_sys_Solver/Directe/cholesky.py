from AlgoNum.Linear_sys_Solver.Directe.Gauss import reduct
from AlgoNum.Linear_sys_Solver.Operations import est_carre, symetrique, show, transpose

m2 = [
    [4, 12, -16, 1],
    [12, 37, -43, 2],
    [-16, -43, 98, 3]
]

import math


def cholesky(mat):
    """
    Factorisation de Cholesky pour une matrice symétrique positive définie A.
    Retourne la matrice triangulaire inférieure L telle que A = L * L^T
    """
    # Vérification de symétrie
    c_mat = [row[:-1] for row in mat]
    if not (symetrique(c_mat) and est_carre(c_mat)):
        if est_carre(c_mat):
            return "La matrice des coefficients n'est pas carée. Gauss Impossible"
        return "Cette matrice n'est pas symétrique."

    n = len(mat)
    b = [row[-1] for row in mat]

    # Initialisation de L avec des zéros
    l = [[0.0] * n for _ in range(n)]


    # Calcul de L
    for i in range(n):
        for j in range(i + 1):
            somme = sum(l[i][k] * l[j][k] for k in range(j))

            if i == j:
                val = mat[i][i] - somme
                if val <= 0:
                    raise ValueError("La matrice n'est pas positive définie.")
                l[i][j] = math.sqrt(val)
            else:
                l[i][j] = (mat[i][j] - somme) / l[j][j]
    show(l)
    u = transpose(l)
    show(u)
    l = list(reversed([list(reversed(row)) for row in l]))
    l_b = [l[i] + [b[-(i+1)]] for i in range(n)]

    # il faut renverser les résultats, car la matrice était au depart triangulaire inférieure avant d'etre modifié pour les calculs
    y = list(reversed(reduct(l_b)))
    u_b = [u[i] + [y[i]] for i in range(n)]

    return reduct(u_b)



# show(cholesky(m2))
