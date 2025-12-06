# ============================================================
#  Programme : OPERATIONS SUR LES MATRICES
#  Auteur    : Héritier ADAKANOU
#  Date      : 26/11/2025
#  Objet     : Quelques operations possibles sur les matrices sont écrites ici sous forme de méthodes que nous utiliserons plus tard
#  Version   : 1.0
#
#  Entrées   : Oui
#  Sorties   : Oui
#
#  Remarques : on pouvait utiliser la bibliothèque numpy mais ce serait bcp trop facile et pas tout à fait portable
#              Les fonctions de ce fichier sont un peu liée les uns aux autres donc il faut un certain ordre pour pouvoir facilement comprendre
#              Un minimum de connaissance sur l'utilisation des tableaux est requise (je dis ça je ne dis rien)
# ============================================================


# matrice de test sur les fonctions (j'ai jugé bon de les laisser)
m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

m2 = [[1, 2, 3],
      [7, 8, 9]]



def taille(m):
    return len(m), len(m[0])

def transpose(m):
    mt = []
    for i in range(len(m[0])):
        mt.append([m[j][i] for j in range(len(m))])
    return mt

def est_carre(m):
    return len(m[0]) == len(m)

def somme(m1, m2):
    if taille(m1) == taille(m2):
        ms = []
        for i in range(len(m1)):
            ms.append([(m1[i][j]+m2[i][j]) for j in range(len(m1[0]))])
        return ms
    else:
        return "Les deux matrices ne sont pas compatible !!"

def matrix_puissance(m, p):
    mm = []
    if est_carre(m):
        for i in range(len(m)):
            mm.append([pow(m[i][j], p)] for j in range(len(m[0])))
        return mm
    else : return "Cette matrice n'est pas carrée !!"

def scalaire(m, x):
    mx = []
    for i in range(len(m)):
        mx.append([m[i][j]*x] for j in range(len(m[0])))
    return mx

def produit(m1,m2):
    if len(m1[0]) == len(m2) :
        m1m2 = []
        for i in range(len(m1[0])):
            m1m2.append([0 for _ in range(len(m1))])
            for j in range(len(m1[0])):
                m1m2[i][j] = m1[i][j] * m2[j][i]
        return m1m2
    else : return "Les deux matrices ne sont pas compatible !!"

def det(m):
    n = len(m)
    if n == 1: # cas où la matrice est ou devient de taille 1*1
        return  m[0][0]
    if n == 2: # cas où la matrice est ou devient de taille 2*2
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]
    d = 0
    for j in range(n):
        mp = [row[:j] + row[j+1:] for row in m[1:]] # suppression de la ligne j et la clone j (simulation vraie)
        signe = (-1)**j # Alternance de signe (-1)**(i+j) avec i = 0 car on a choisis de faire le determinant avec la premiere ligne
        d += signe * m[0][j] * det(mp) # on fait la récursivité tout comme ça se fait sur papier avec les sous matrice du det precedent
    return d

def egal(m1, m2):
    return m1 == m2

def tt_inconnue(liste):
    for i in liste[:-1]:
        if i == 0 :
            return False
    return True

def pivot_partiel(mat,niveau):
    max_coef = niveau
    for i in range(niveau, len(mat)):
        if abs(mat[i][niveau]) > abs(mat[max_coef][niveau]) and tt_inconnue(mat[i][niveau:]):
            max_coef = i
            print(f"Le maxCoef = {i}")
    mat[niveau], mat[max_coef] = mat[max_coef], mat[niveau]
    return mat

def show(mat):
    for row in mat:
        print(row)
    print('\n')