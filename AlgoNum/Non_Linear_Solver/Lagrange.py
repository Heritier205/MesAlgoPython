# Interpolation polynomiale de Lagrange avec affichage du polynôme

# 1. Saisie des points
n = int(input("Nombre de points : "))

x_vals = []
y_vals = []

for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    x_vals.append(x)
    y_vals.append(y)

# 2. Saisie du point à interpoler
x = float(input("Valeur de x à interpoler : "))

# 3. Calcul du polynôme
P = 0
polynome_str = ""  # pour construire une représentation textuelle

for i in range(n):
    Li = 1
    Li_terms = []  # pour afficher L_i(x)
    for j in range(n):
        if i != j:
            Li *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
            Li_terms.append(f"(x - {x_vals[j]})/({x_vals[i]} - {x_vals[j]})")
    P += y_vals[i] * Li

    # Ajouter L_i(x) au polynôme en texte
    polynome_str += f"{y_vals[i]}*({'*'.join(Li_terms)})"
    if i != n-1:
        polynome_str += " + "

# 4. Affichage
print(f"\nPolynôme de Lagrange :\nP(x) = {polynome_str}")
print(f"\nValeur interpolée en x = {x} : {P}")
