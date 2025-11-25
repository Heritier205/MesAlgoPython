# ============================================================
#  Programme : RESOLUTION PROBLEME DU SAC A DOS ( KNAPSACK ) 0/1
#  Auteur    : Héritier ADAKANOU , BEDEL Josué
#  Date      : 25/11/2025
#  Objet     : Il s'agit d'un programme qui resous le probleme du sac a dos (KNAPSACK)
#  Version   : 1.0
#
#  Entrées   : Oui
#  Sorties   : Oui
#
#  Remarques :
# ============================================================

def KnapsackBinaire(W, w, v, n):
    DP = [[0 for i in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if w[i-1] <= j:
                DP[i][j] = max(DP[i-1][j] ,DP[i-1][j-w[i-1]] + v[i-1])
            else :
                DP[i][j] = DP[i-1][j]

    return DP


def getInt(msg):
    while True:
        try :
            n = int(input(f"Entrez {msg} (n > 0) : "))
            if n <= 0 :
                raise ValueError
            return n
        except (TypeError, ValueError):
            print("Invalide !!")
            continue



def main():
    print(f"""{'-'*6}RESOLUTION PROBLEME DU SAC A DOS{'-'*6}\n
    Bienvenue dans ce programme 
""")
    W = getInt("la capacité totale du sac")
    n = getInt("le nombre total d'objets")
    print("\n")
    w, v = [0]*n, [0]*n
    for i in range(n):
        w[i] = getInt(f"Entrez le poids de l'ojet {i+1}")
        v[i] = getInt(f"Entrez la valeur l'objet {i+1}")
        print("\n")
    DP = KnapsackBinaire(W, w, v, n)
    for dp in DP:
        print(dp)
    print("\nFin du programme !!")

while True:
    main()
    r = input("Voulez vous recommencer (y/N) : ")
    if  r != "y" and r != "Y" :
        break



