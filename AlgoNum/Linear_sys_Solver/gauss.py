import math

def afficher_matrice(A):
    for ligne in A:
        print("\t".join(f"{val:.10f}" for val in ligne))

def afficher_vecteur(B):
    print("\t".join(f"{val:.2f}" for val in B))

continuer = True

while continuer:
    # Saisie du rang de la matrice A
    while True:
        n = int(input("Saisissez le rang de la matrice A (n x n) : "))
        if n > 0:
            break
        print("Invalide ! Ressaisissez une valeur positive !")

    # Déclaration dynamique des tableaux
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    B = [0.0 for _ in range(n)]
    X = [0.0 for _ in range(n)]
    det = 1.0
    permutations = 0

    # Saisie de la matrice A
    print(f"Saisissez les coefficients de la matrice A ({n} x {n}) :")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"A[{i}][{j}]: "))

    # Saisie du vecteur B
    print(f"Saisissez les coefficients du vecteur B ({n} x 1) :")
    for i in range(n):
        B[i] = float(input(f"B[{i}]: "))

    # Affichage de la matrice et du vecteur sous forme de tableau
    print("\nMatrice A :")
    afficher_matrice(A)
    print("\nVecteur B :")
    afficher_vecteur(B)

    # Élimination de Gauss avec pivot partiel
    for k in range(n - 1):
        pivot_row = k
        max_val = abs(A[k][k])
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_val:
                max_val = abs(A[i][k])
                pivot_row = i

        if max_val == 0:
            det = 0
            print("\nPivot nul détecté, système singulier.")
            break

        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            B[k], B[pivot_row] = B[pivot_row], B[k]
            permutations += 1

        det *= A[k][k]

        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(n):
                A[i][j] -= factor * A[k][j]
            B[i] -= factor * B[k]

    det *= A[n - 1][n - 1]
    if permutations % 2 != 0:
        det = -det

    print(f"\nLe determinant de A est : {det:.2f}")

    if det == 0:
        print("Le determinant est nul.")
        print("=> La matrice A est singulière (non inversible).")
        print("=> Le système AX = B n’a pas de solution unique.")
        print("=> Possibilités :")
        print("   - Aucune solution (système incompatible)")
        print("   - Infinité de solutions (système indéterminé)")
        print("\nConclusion :")
        print("Comme det(A) = 0, le système n'est pas régulier. Impossible de garantir une solution unique.")
    else:
        # Rétro-substitution
        for i in range(n - 1, -1, -1):
            X[i] = B[i]
            for j in range(i + 1, n):
                X[i] -= A[i][j] * X[j]
            X[i] /= A[i][i]

        print("\nLa solution X de l'équation AX = B est :")
        afficher_vecteur(X)

        print("\nConclusion :")
        print("Comme det(A) ≠ 0, la matrice A est inversible.")
        print("=> Le système possède une solution unique.")

    # Demander si on veut recommencer
    rep = input("\nVoulez-vous résoudre un autre système ? (o/N) : ").strip().lower()
    if rep != 'o':
        continuer = False

print("\nFin du programme.")
