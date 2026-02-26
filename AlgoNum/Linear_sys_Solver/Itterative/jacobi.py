from AlgoNum.Linear_sys_Solver.Operations import show

m2 = [
    [10, -1,  2,  6],
    [-1, 11, -1, 25],
    [ 2, -1, 10, -11]
]



def jacobi(mat, x0=None, tol=1e-10, max_iter=1000):
    """
    Résout Ax = b par la méthode de Jacobi
    A : matrice carrée
    b : vecteur
    x0 : vecteur initial (None => zéro)
    tol : tolérance pour convergence
    max_iter : nombre maximal d'itérations
    """
    b = [row[-1] for row in mat]
    c_mat = [row[:-1] for row in mat]
    n = len(mat)
    x = [0.0]*n if x0 is None else x0[:]
    x_new = x[:]

    for iteration in range(max_iter):
        for i in range(n):
            s = sum(c_mat[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / c_mat[i][i]

        # Vérifier convergence
        diff = max(abs(x_new[i] - x[i]) for i in range(n))
        if diff < tol:
            return x_new

        x[:] = x_new[:]

        show(x_new)

    return f"Jacobi n'a pas convergé après {max_iter} itérations"

# show(jacobi(m2))