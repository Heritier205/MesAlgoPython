m_good = [
    [10, -1,  2,  6],
    [-1, 11, -1, 25],
    [ 2, -1, 10, -11]
]



def gauss_seidel(mat, x0=None, tol=1e-10, max_iter=1000):
    b = [row[-1] for row in mat]
    c_mat = [row[:-1] for row in mat]
    n = len(c_mat)

    x = [0.0] * n if x0 is None else x0[:]

    for iteration in range(max_iter):
        x_old = x[:]

        for i in range(n):
            s1 = sum(c_mat[i][j] * x[j] for j in range(i))  # nouvelles valeurs
            s2 = sum(c_mat[i][j] * x_old[j] for j in range(i + 1, n))  # anciennes valeurs

            x[i] = (b[i] - s1 - s2) / c_mat[i][i]

        # test de convergence
        diff = max(abs(x[i] - x_old[i]) for i in range(n))
        if diff < tol:
            return x

    return f"Gauss-Seidel n'a pas convergé après {max_iter} itérations"

print(gauss_seidel(m_good))
