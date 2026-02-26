from AlgoNum.Linear_sys_Solver.Gauss import reduct
from AlgoNum.Linear_sys_Solver.Operations import est_carre, show, pivot_partiel

m2 = [
    [0, 2, 9, 1],
    [1, -1, 2, 0],
    [3, 2, -1, 4]
]




def crout_decomp(mat):
    if not est_carre([row[:-1] for row in mat]) :
        return "La matrice des coefficients n'est pas carée. Gauss Impossible"
    else :
        n = len(mat)
        l = [[0]*n for _ in mat]
        u = [[0]*n for _ in mat]
        for i in range(n):
            mat = pivot_partiel(mat, i)
        for i in range(n):
            # Calcul de U[i][j]
            for j in range(i, n):
                s = sum(l[i][k] * u[k][j] for k in range(i))
                u[i][j] = mat[i][j] - s
            # Calcul de L[k][i]
            for k in range(i, n):
                s = sum(l[k][j] * u[j][i] for j in range(i))
                l[k][i] = (mat[k][i] - s) / u[i][i]

        return l, u, mat

def crout(mat):
    l, u, mat = crout_decomp(mat)
    b = [row[-1] for row in mat]

    # ici, je veux utiliser une fonction que j'ai deja et qui est t capable de résoudre les matrice triangulaire
    # Vu que je n'ai pas trop envie de réécrire une fonction de substitution pour chaque type de matrice,
    # je vais juste transformer cette matrice qui sera toujours triangulaire inférieure en supérieure pour utiliser ma fonction
    l = list(reversed(l))
    l = [list(reversed(row)) for row in l]
    # je ne fais pas de transformation au niveau de u, car de base, il sera toujours triangulaire supérieure

    l_b = [l[i] + [b[-(i+1)]] for i in range(len(b))]
    y = reduct(l_b)
    u_b = [u[i] + [y[i]] for i in range(len(y))]

    return reduct(u_b)



# show(crout(m2))