def projet_calculatrice():
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    while not a.isdigit() or not b.isdigit():
        print("Veuillez entrer deux nombres valides.")
        a = input("Entrez un premier nombre : ")
        b = input("Entrez un deuxième nombre : ")
    else:
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}.")

    """
    Autre solution :
    (On déclare deux variables)
    a = b = ""
    (Tant que a et b ne sont pas des nombres, on boucle)
    while not (a.isdigit() and b.isdigit()):
    (On demande deux nombres à l'utilisateur)
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    (On affiche une phrase si les nombres entrés ne sont pas valides.)
    if not (a.isdigit() and b.isdigit()):
    print("Veuillez entrer deux nombres valides")
    (On affiche le résultat de l'addition)
    print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
    """


def projet_liste_course():
    # INFOS DE DEPART :
    import json
    chemin = r"liste_course.json"
    choix = ""

    # BOUCLE MENU PRINCIPAL :
    while choix != "5":

        print("\nChoississez parmi les cinq options suivantes :\n 1 = Ajouter un élément à la liste de courses\n 2 = "
              "Retirer un élément de la liste de courses\n 3 = Afficher les éléments de la liste de courses\n 4 = "
              "Vider la liste de courses\n 5 = Quitter le programme")
        choix = input("\nEntrez votre choix : ")

        with open(chemin, "r") as liste_de_course:
            contenu = json.load(liste_de_course)

        # CHOIX 1 : AJOUTER UN ELEMENT
        if choix == "1":
            element = input("\nElement à ajouter : ")
            sur: str = ""
            if element in contenu:
                while sur not in ["oui", "non"]:
                    sur = input("Cet élément existe déjà dans votre liste. Si vous souhaitez quand-même l'ajouter, "
                                "tapez oui, sinon, tapez non. ")
            if sur != "non":
                contenu.append(element)
                with open(chemin, "w") as liste_de_course:
                    json.dump(contenu, liste_de_course, indent=4)
                print(f"\n'{element}' a bien été ajouté à votre liste.")

        # CHOIX 2 : ENLEVER UN ELEMENT
        elif choix == "2":
            element = input("\nElement à enlever : ")
            while (element not in contenu) and (element != "stop"):
                element = input(
                    "\nElement introuvable. Veuillez entrer un élément faisant partie de votre liste de course ou "
                    "annuler en tapant stop : ")
            if element != "stop":
                contenu.remove(element)
                with open(chemin, "w") as liste_de_course:
                    json.dump(contenu, liste_de_course, indent=4)
                print(f"\n'{element}' a bien été enlevé de votre liste")

        # CHOIX 3 : MONTRER LA LISTE
        elif choix == "3":
            liste_colonne = "\n".join(contenu)
            print(f"\nVotre liste de course contient :\n{liste_colonne}")

        # CHOIX 4 : VIDER LA LISTE
        elif choix == "4":
            sur = ""
            while sur not in ["oui", "non"]:
                sur = input("Etes-vous sûr ? Ce choix est irréversible. Pour continuer, tapez oui, sinon, tapez non : ")
            if sur == "oui":
                contenu.clear()
                with open(chemin, "w") as liste_de_course:
                    json.dump(contenu, liste_de_course, indent=4)
                print("\nLa liste de course a bien été vidée.")

        # CHOIX NON VALIDE
        elif not choix.isdigit() or 0 < int(choix) > 5:
            print("\nVeuillez entrer un chiffre entre 1 et 5.")

        print("-" * 50)

        # CHOIX 5 : QUITTER
    print("\nA bientôt!")


def projet_nombre_mystere():
    print("*** Le jeu du nombre mystère ***")
    import random
    nombre_mystere = random.randrange(101)
    nombre_essai: int = 5
    essai_joueur: int = int()

    while essai_joueur != nombre_mystere and nombre_essai > 0:
        print(f"Il vous reste {nombre_essai} essais pour trouver le nombre mystère.")
        user_text: str = input("Entrez un nombre entre 0 et 100 : ")

        while not user_text.isdigit() or not 0 <= int(user_text) <= 100:
            print(f"Il vous reste {nombre_essai} essais pour trouver le nombre mystère.")
            user_text = input("Entrez un nombre entre 0 et 100 : ")
        essai_joueur = int(user_text)
        nombre_essai -= 1

        if nombre_essai > 0:
            if nombre_mystere < int(essai_joueur):
                print(f"Le nombre mystère est plus petit que {essai_joueur}.")
            elif nombre_mystere > int(essai_joueur):
                print(f"Le nombre mystère est plus grand que {essai_joueur}.")

    if essai_joueur == nombre_mystere:
        print(f"Bravo, le nombre mystère était bien {nombre_mystere} ! \n"
              f"Vous l'avez trouvé en {5 - nombre_essai} essais.\nLe jeu est terminé.")
    else:
        print(f"Dommage ! Le nombre mystère était {nombre_mystere}.\nLe jeu est terminé.")

    """
    MOI :

    def projet4():
        print("*** Le jeu du nombre mystère ***")
        import random
        nombre_mystere = random.randrange(101)
        nombre_essai: int = 5
        essai_joueur: int = int()
        print(nombre_mystere)
        while essai_joueur != nombre_mystere:
            print(f"Il vous reste {nombre_essai} essais pour trouver le nombre mystère.")
            user_text: str = input("Entrez un nombre entre 0 et 100 : ")

            while not user_text.isdigit() or not 0 <= int(user_text) <= 100:
                print(f"Il vous reste {nombre_essai} essais pour trouver le nombre mystère.")
                user_text = input("Entrez un nombre entre 0 et 100 : ")
            essai_joueur = int(user_text)
            nombre_essai -= 1

            if nombre_essai < 1:
                print(f"Dommage ! Le nombre mystère était {nombre_mystere}.\nLe jeu est terminé.")
                break
            elif nombre_mystere < int(essai_joueur):
                print(f"Le nombre mystère est plus petit que {essai_joueur}.")
            elif nombre_mystere > int(essai_joueur):
                print(f"Le nombre mystère est plus grand que {essai_joueur}.")

        if nombre_mystere == int(essai_joueur):
                print(f"Bravo, le nombre mystère était bien {nombre_mystere} ! \n"
                      f"Vous l'avez trouvé en {5 - nombre_essai} essais.\nLe jeu est terminé.")

    THIBAULT :

    from random import randint

    number_to_find = randint(0, 100)
    remaining_attempts = 5

    print("*** Le jeu du nombre mystère ***")

    # Boucle principale
    while remaining_attempts > 0:
        print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

        # Saisie de l'utilisateur
        user_choice = input("Devine le nombre : ")
        if not user_choice.isdigit():
            print("Veuillez entrer un nombre valide.")
            continue

        user_choice = int(user_choice)    

        if number_to_find > user_choice:  # Plus grand
            print(f"Le nombre mystère est plus grand que {user_choice}")
        elif number_to_find < user_choice:  # Plus petit
            print(f"Le nombre mystère est plus petit que {user_choice}")
        else:  # Égal (succès)
            break

        remaining_attempts -= 1

    # Gagné ou perdu
    if remaining_attempts == 0:
        print(f"Dommage ! Le nombre mystère était {number_to_find}")
    else:
        print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
        print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")

    print("Fin du jeu.")
    """


def projet_jeu_de_role():
    import random
    # Stat de départ :
    vie_joueur: int = 50
    vie_ennemi: int = 50
    nombre_potion: int = 3
    skip = False

    while vie_joueur > 0 and vie_ennemi > 0:
        attaque_joueur: int = random.randint(5, 10)
        attaque_ennemi: int = random.randint(5, 15)
        bonus_potion: int = random.randint(15, 50)
        choix: str = ""

        if not skip:
            while choix != "1" and (choix != "2" or nombre_potion == 0):
                if choix == "2" and nombre_potion == 0:
                    print("Vous n'avez plus de potions.")
                choix: str = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

            if choix == "1":
                vie_ennemi -= attaque_joueur
                print(f"Vous avez infligé {attaque_joueur} points de dégats à l'ennemi.")
            else:  # choix == "2"
                skip = True
                nombre_potion -= 1
                vie_joueur = min(50, vie_joueur + bonus_potion)
                if vie_joueur == 50:
                    print("Vous avez réccupéré toute votre vie.")
                else:
                    print(f"Vous avez réccupéré {bonus_potion} points de vie.")
        else:
            print("Vous passez votre tour.")
            skip = False

        if vie_ennemi > 0:
            vie_joueur -= attaque_ennemi
            print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats.")

        if vie_joueur > 0 and vie_ennemi > 0:
            print(f"Il vous reste {vie_joueur} points de vie.\nIl reste {vie_ennemi} points de vie à "
                  f"l'ennemi.\n\n{'-' * 30}\n")

    if vie_joueur <= 0:
        print("Dommage, vous avez perdu.")
    else:
        print(f"Bravo, vous avez gagné avec {vie_joueur} points de vie restant.")

    # ANCIENNES VERSIONS JEU DE ROLE
    """import random
    # Stat de départ :
    vie_joueur: int = 50
    vie_ennemi: int = 50
    nombre_potion_depart: int = 3
    nombre_potion: int = 3
    
    while vie_joueur > 0 and vie_ennemi > 0:
        attaque_joueur: int = random.randint(5, 10)
        attaque_ennemi: int = random.randint(5, 15)
        bonus_potion: int = random.randint(15, 50)
        choix: str = ""
    
        if nombre_potion == nombre_potion_depart:

            while choix != "1" and choix != "2":
                choix: str = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

            while nombre_potion == 0 and choix != "1":
                if choix == "2":
                    print("Vous n'avez plus de potions.")
                choix: str = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

            if choix == "1":
                vie_ennemi -= attaque_joueur
                print(f"Vous avez infligé {attaque_joueur} points de dégats à l'ennemi.")
            elif choix == "2":
                nombre_potion -= 1
                vie_joueur += bonus_potion
                if vie_joueur > 50:
                    vie_joueur = 50
                    print("Vous avez réccupéré toute votre vie.")
                else:
                    print(f"Vous avez réccupéré {bonus_potion} points de vie.")

        else:
            print("Vous passez votre tour.")
            nombre_potion_depart -= 1

        if vie_ennemi > 0:
            vie_joueur -= attaque_ennemi
            print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats.")

        if vie_joueur > 0 and vie_ennemi > 0:
            print(f"Il vous reste {vie_joueur} points de vie.\nIl reste {vie_ennemi} points de vie à "
                  f"l'ennemi.\n\n-----------------------------------------------------------------------"
                  f"-------------------------------------\n")

    if vie_joueur <= 0:
        print("Dommage, vous avez perdu.")
    else:
        print(f"Bravo, vous avez gagné avec {vie_joueur} points de vie restant.")
        
        #CORRECTION THIBAULT :
        ENEMY_HEALTH = 50
        PLAYER_HEALTH = 50
        NUMBER_OF_POTIONS = 3
        SKIP_TURN = False
        
        while True:
            # Jeu du joueur
            if SKIP_TURN:
                print("Vous passez votre tour...")
                SKIP_TURN = False
            else:
                user_choice = ""
                while user_choice not in ["1", "2"]:
                    user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        
                if user_choice == "1":  # Attaque
                    your_attack = random.randint(5, 10)
                    ENEMY_HEALTH -= your_attack
                    print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔️")
                elif user_choice == "2" and NUMBER_OF_POTIONS > 0:  # Potion
                    potion_health = random.randint(15, 50)
                    PLAYER_HEALTH += potion_health
                    NUMBER_OF_POTIONS -= 1
                    SKIP_TURN = True
                    print(f"Vous récupérez {potion_health} points de vie ❤️ ({NUMBER_OF_POTIONS} ? restantes)")
                else:
                    print("Vous n'avez plus de potions...")
                    continue
        
            if ENEMY_HEALTH <= 0:
                print("Tu as gagné ?")
                break
        
            # Attaque de l'ennemi
            enemy_attack = random.randint(5, 15)
            PLAYER_HEALTH -= enemy_attack
            print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")
        
            if PLAYER_HEALTH <= 0:
                print("Tu as perdu ?")
                break
        
            # Stats
            print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
            print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi.")
            print("-" * 50)
        
        print("Fin du jeu.")"""


def projet_tri_fichiers():
    from pathlib import Path

    # Choisir mon dossier Download:
    dossier_download = Path(r"C:\Users\Eva Boland\Downloads")

    # Obtenir une liste des extensions qui s'y trouvent:
    for f in dossier_download.iterdir():
        print(f.suffix)

    # Créer un dictionnaire liant ces extensions à un nom de dossier:
    mon_tri = {".pdf": "Documents",
               ".jpg": "Images",
               ".docx": "Documents",
               ".xlsx": "Documents",
               ".ini": "Autres",
               ".mp3": "Musique",
               ".exe": "Applications",
               ".png": "Images",
               ".zip": "Autres"}

    # Réccupérer tous les fichiers dans Download :
    my_files = [file for file in dossier_download.iterdir() if file.is_file()]

    # Boucle sur ces fichiers pour les déplacer :
    for file in my_files:
        dossier_tri = dossier_download / mon_tri.get(file.suffix, "Autres")    # Si le suffix d'un fichier n'est pas
        # dans le dictionnaire mon_tri, le fichier ira dans "Autre"
        dossier_tri.mkdir(exist_ok=True)    # Création du dossier
        file.rename(dossier_tri / file.name)  # .rename permet de déplacer le fichier en renommant le chemin vers lui






if __name__ == '__main__':

