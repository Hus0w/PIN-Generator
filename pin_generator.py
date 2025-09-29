import random

while True:
    user_input = input("Entrez le nombre de caractères pour votre code PIN (4, 5 ou 6) : \n")
    try:
        n = int(user_input)
    except ValueError:
        print("ERREUR : merci d'entrer un entier (4, 5 ou 6) ! \n")
        continue

    if n == 4:
        pin = random.randint(1000, 9999)
        print("Voici le code PIN généré :", pin)
        break
    elif n == 5:
        pin = random.randint(10000, 99999)
        print("Voici le code PIN généré :", pin)
        break
    elif n == 6:
        pin = random.randint(100000, 999999)
        print("Voici le code PIN généré :", pin)
        break
    else:
        print("Mauvais input, veuillez réessayez.. \n")