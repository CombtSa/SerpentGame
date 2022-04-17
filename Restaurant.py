# Bienvenue
import main


def Restaurant():
    print("Bienvenue dans le restaurant")
    # Panier
    panier = 0
    argent = 1000

    print("Voici le menu:")
    # Menu 1
    print("Fast-food : 15$")
    Fast_food = False
    achat = input('Voulez-vous lacheter ?')
    if argent < 15:
        print("Vous ne pouvez pas acheter ce menu")
    if achat == 'Oui':
        Fast_food = True
        panier += 0.5
    elif achat == 'Non':
        Fast_food = False
        panier = 0
    else:
        print("Je n'ai pas compris")

    savoir = input('Voulez-vous en savoir plus taper FF')
    if savoir == 'FF':
        print("Le menu contient un hamburger classic, des frites et une boisson")
    elif savoir == 'Non':
        print("Ok")
    else:
        print("Je n'ai pas compris")

    # Menu 2

    print("Menu Francais : 30$")
    achat_1 = input('Voulez-vous lacheter ?')
    if argent < 30:
        print("Vous ne pouvez pas acheter ce menu")
    if achat_1 == 'Oui':
        Fast_food = True
        panier += 1
    elif achat_1 == 'Non':
        Fast_food = False
        panier = 0
    else:
        print("Je n'ai pas compris")

    savoir_1 = input('Voulez-vous en savoir plus taper MF')
    if savoir_1 == 'MF':
        print("le menu contient une raclette")
    elif savoir_1 == 'Non':
        print("Ok")
    else:
        print("Je n'ai pas compris")

    print("Menu Allemand  : 30$")
    achat_3 = input('Voulez-vous lacheter ?')
    if argent < 20:
        print("Vous ne pouvez pas acheter ce menu")
    if achat_1 == 'Oui':
        Fast_food = True
        panier += 1
    elif achat_1 == 'Non':
        Fast_food = False
        panier = 0
    else:
        print("Je n'ai pas compris")
    if panier == 1.5:
        print("Le Panier est le Menu Fast-Food et le Menu Francais")
    elif panier == 1:
        print("Le panier est le Menu Francais")
    elif panier == 0.5:
        print("Le Panier est le Menu Fast-Food")

    result = input('Tout est bon')
    if result == 'Oui':
        achat = True
    elif result == 'Non':
        achat = False
        main.Start()

    argent_total = argent - 35
    argent_total = float(argent_total)
    argent_total_1 = argent - 20
    argent_total_2 = argent - 15

    if achat == True:
        if panier == 1.5:
            print("Le prix est de 35$")
            print("Il vous reste: ", argent_total, "$")
        elif panier == 1:
            print("Le prix est", argent_total_1)
            print("Il vous reste: ", argent_total_1, "$")
        elif panier == 0.5:
            print("Le prix est", argent_total_2)
            print("Il vous reste: ", argent_total_2, "$")
        else:
            print("Je n'ai pas compris")

    print(argent_total, argent_total_1, argent_total_2)
    argent_total += argent_total_1
    argent_total += argent_total_2

    stastique = argent_total / 100

    stastique = str(stastique)

    with open("code.txt", "a", encoding="utf8") as fichier:
        fichier.write(stastique)
        fichier.write('\n')
