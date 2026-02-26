from fractions import Fraction

from Operations import *
m2 = [
    [0, 2, 9, 1],
    [1, -1, 2, 0],
    [3, 2, -1, 4]
]
m1 = [
    [1, 1, 2, 9],
    [2, 4, -3, 1],
    [3, 6, -5, 0]
]
m3 = [
    [4, 12, -16, 1],
    [12, 37, -43, 2],
    [-16, -43, 98, 3]
]


def gauss(mat):
    if not est_carre([row[:-1] for row in mat]) :
        return "La matrice des coefficients n'est pas carée. Gauss Impossible"
    else :
        mat = pivot_partiel(mat,0)
        n = len(mat)
        for i in range(n-1): # on fixe la premiere ligne et on boucle sur les n-1 restant
            pivot = mat[i][i] # Comprehensible heun ...
            for k in range(i+1, n): # On boucle sur les lignes en dessous du pivot actuel
                fact = mat[k][i]/pivot # Le facteur est donc le rapport des premiere colones non nul
                for j in range(n+1): # on boucle sur chaque colones y compris les colones solution
                    mat[k][j] -= fact*mat[i][j] # multiplication et remplissage des colones
            mat = pivot_partiel(mat, i+1) # On refait le pivot à chaque étape
    show(mat)
    return reduct(list(mat))




def reduct(mat):
    s_mat = []
    while len(mat) > 0:
        s_mat.append(mat[-1][-1]/mat[-1][-2])

        mat = mat[:-1]
        for i in range(len(mat)):
            mat[i][-1] -= mat[i][-2]*s_mat[-1]
        mat = [row[:-2]+row[-1:] for row in mat]
    return list(reversed(s_mat))

# show(gauss(m3))








