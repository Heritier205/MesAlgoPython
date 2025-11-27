
from pointFixe import point_fixe, point_fixe2
from ballayage import dichotomie
from secante import secante
from newton import newton


choice= ''

while choice != "N" or choice != "n" :
    pas = float(input("\nEntrez le pas : "))
    print("""\n\n           
                Les methodes de resolution sont  \n
                1) Methode de substitution ou point fixe 
                2) Methode de  dichotomie
                3) Methode de la corde ou secante
                4) Methode de newton 
    """)

    answer = input("Quelle methode aimeriez vous utiliser ? (1-4) : ")
    match answer:
        case '1':
            x = float(input("Entrez un x0 : "))
            print(point_fixe(x, pas))
        case '2':
            a = float(input("Entrez un premier point inf : "))
            b = float(input("Entrez un deuxieme point sup : "))
            print(dichotomie(a, b, pas))
        case '3':
            x0 = float(input("Entrez un premier point a : "))
            x1 = float(input("Entrez un deuxieme point b : "))
            print(secante(x0, x1, pas))
        case '4':
            x0 = float(input("Entrez un x0 : "))
            print(newton(x0, pas))
        case "all":
            x = float(input("\nEntrez un x0 : "))
            print(point_fixe(x, pas))

            a = float(input("\nEntrez un premier point inf : "))
            b = float(input("Entrez un deuxieme point sup : "))
            print(dichotomie(a, b, pas))

            x0 = float(input("\nEntrez un premier point a : "))
            x1 = float(input("Entrez un deuxieme point b : "))
            print(secante(x0, x1, pas))

            x0 = float(input("\nEntrez un x0 : "))
            print(newton(x0, pas))
    choice = input("\nVoulez-vous essayer  (y/n) ? ")

