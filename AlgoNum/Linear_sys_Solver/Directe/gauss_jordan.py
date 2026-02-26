from AlgoNum.Linear_sys_Solver.Operations import est_carre, pivot_partiel, show

m2 = [[1, 1, 1, 6],
      [2, -1, 1, 3],
      [1, 2, -1, 3]]
m1 = [
    [1, 1, 2, 9],
    [2, 4, -3, 1],
    [3, 6, -5, 0]
]


def gauss_jordan(mat) :
    if not est_carre([row[:-1] for row in mat]):
        return "La matrice des coeficients n'est pas carée. Gauss Impossible"
    else:
        mat = pivot_partiel(mat, 0)
        n = len(mat)
        for i in range(n):
            mat = pivot_partiel(mat, i)
            pivot = mat[i][i]
            for k in range(n+1):
                mat[i][k] /= pivot
            for j in range(n):
                if i != j :
                    factor = mat[j][i]
                    for k in range(n+1):
                        mat[j][k] -= factor * mat[i][k]
        return [s[-1] for s in mat]



show(gauss_jordan(m1))