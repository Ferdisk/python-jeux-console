import Existe, getpass

class bcolors:
    """
    Classe contenant des codes ANSI pour styliser le texte dans le terminal.
    Utilisée pour changer la couleur des messages dans la console.

    Attributs :
        GREEN (str) : Code pour le texte vert.
        YELLOW (str) : Code pour le texte jaune.
        RED (str) : Code pour le texte rouge.
        RESET (str) : Code pour réinitialiser le style du texte.
        MAGENTA (str) : Code pour le texte magenta.
    """
    GREEN = "\033[92m"  
    YELLOW = "\033[93m"  
    RED = "\033[91m"  
    RESET = "\033[0m"  
    MAGENTA = '\033[35m'

class Joueur:
    """
    Représente un joueur participant à un jeu.

    Attributs :
        nom (str) : Nom du joueur.
        score (int) : Score actuel du joueur.
    """
    nom: str
    score: int
    
class Jeux:
    """
    Représente un jeu.

    Attributs :
        tab_score (list[Joueur]) : Tableau contenant les scores des joueurs pour ce jeu. 
        nb_joueur (int] : Nombre de joueurs diffèrents ayant joué à ce jeu. 
    """
    tab_score : list[Joueur]
    nb_joueur: int

class Score:
    """
    Contient les scores pour différents jeux.

    Attributs :
        Devinette (Jeux) : Scores associés au jeu "Devinette".
        Morpion (Jeux) : Scores associés au jeu "Morpion".
        Allumettes (Jeux) : Scores associés au jeu "Allumettes".
    """
    Devinette: Jeux
    Morpion: Jeux
    Allumettes: Jeux


def devinette(j1: str, j2: str, Score_jeux: Score) -> None:
    """Procédure qui éxécute le jeu de la devinette

    Args:
        j1 (str): chaine de caractère représentant le joueur jouant en premier
        j2 (str): chaine de caractère représentant le joueur jouant en deuxième_
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    limite: int
    reponse: int
    tour = 1
    choix: int
    phr_victoire: str
    test_regle: int
    regle: str
    existe: list[int]


    joueur1: Joueur
    joueur2: Joueur
    joueur1 = Joueur()
    joueur2 = Joueur()
    joueur1.nom = j1
    joueur1.score = 0
    joueur2.score = 10
    joueur2.nom = j2

    trouver: bool
    trouver = False

    # Vérification de l'existence des joueurs dans la liste des scores et les ajoute si ce n'est pas le cas 
    existe = Existe.Joueur_existe(j1, j2, Score_jeux,"Allumettes")

    # Règles du jeu de la devinette 
    regle = (f"{bcolors.MAGENTA}Le joueur 1 choisi un nombre entre 1 et une limite à décider. "
             "Le joueur 2 doit deviner ce nombre : à "
             f"chacune de ses propositions, le joueur 1 répond 'trop petit', \n'trop grand', ou 'c'est gagné'.{bcolors.RESET}\n")

    # Demande si le joueur a besoin des règles du jeu  
    test_regle = int(input("Avez-vous besoin des règles du jeux, répondez positivement par 1 sinon 2:\n"))
    while test_regle != 1 and test_regle != 2:
        test_regle = int(input("Vous devez répondre positivement par 1 sinon 2: \n"))

    # Affichage des règles du jeu si besoin 
    if test_regle == 1:
        print(regle)

    phr_victoire = "C'est gagné"

    # Demande de la limite du nombre à deviner  
    limite = int(input(f"{bcolors.YELLOW}Joueur 1 {j1}{bcolors.RESET}: Veuillez choisir la limite : \n"))
    # Vérification de la limite qui doit être un nombre positif strictement supérieur à 1 ou égal à 1 
    while limite <= 1:
        limite = int(input(f"{bcolors.RED}Votre limite doit être un nombre positif strictement supérieur à 1 : \n{bcolors.RESET}"))
    print(f"{bcolors.RED}Votre nombre se situe entre 1 et {limite} {bcolors.RESET}")

    # Demande du nombre à deviner et empêche l'affichage du nombre à deviner lors de la saisie et dans la console avec getpass
    reponse = int(getpass.getpass(f"{bcolors.GREEN}Joueur 1 {j1}{bcolors.RESET} : Choisissez le nombre à deviner: \n"))
    
    # Vérification du nombre à deviner qui doit être compris entre 1 et la limite
    while reponse > limite or reponse < 1:
        print(f"{bcolors.RED}Vous devez choisir un nombre entre 1 et", limite)
        reponse = int(getpass.getpass(f"{bcolors.GREEN}Joueur 1 {j1}{bcolors.RESET} : Choisissez le nombre à deviner: \n"))
    
    # Boucle principale du jeu qui continue jusqu'à ce que le nombre soit trouvé
    while not trouver:
        print(f"{bcolors.GREEN}Joueur 2 {j2} {bcolors.RESET}: à vous de jouer ")
        print(f"{bcolors.RED}C'est votre essaie numéro", tour)
        choix = int(input(f"{bcolors.RESET}Entrer un nombre entre, 1 et {limite}\n"))
        # Test si le nombre choisi est plus petit que le nombre à deviner 
        if reponse > choix:
            print(f"{bcolors.RED}Trop petit\n{bcolors.RESET}")
            # Incrémentation du score du joueur 1 et décrémentation du score du joueur 2
            if joueur1.score != 10 and joueur2.score != 0:
                joueur1.score += 1
                joueur2.score -= 1
        # Test si le nombre choisi est plus grand que le nombre à deviner
        elif reponse < choix:
            print(f"{bcolors.RED}Trop grand\n{bcolors.RESET}")
            # Incrémentation du score du joueur 1 et décrémentation du score du joueur 2
            if joueur1.score != 10 and joueur2.score != 0:
                joueur1.score += 1
                joueur2.score -= 1
        # Test si le nombre choisi est égal au nombre à deviner
        elif choix == reponse:
            print(f"{bcolors.RED}La réponse était bien {reponse}{bcolors.RESET}")
            print(f"{bcolors.YELLOW}{phr_victoire} {bcolors.RESET}avec {bcolors.GREEN}{joueur2.score} pour {j2} {bcolors.RESET}et {bcolors.YELLOW}{joueur1.score} pour {j1} {bcolors.RESET}\n")
            # Sortie de la boucle principale du jeu 
            trouver = True
        # Incrémentation du tour
        tour += 1
    # Ajout des joueurs à la liste des scores
    if existe[0] == -1:
        Score_jeux.Devinette.tab_score.append(joueur1)
    else:
        Score_jeux.Devinette.tab_score[existe[0]].score += joueur1.score
    if existe[1] == -1:
        Score_jeux.Devinette.tab_score.append(joueur2)
    else:
        Score_jeux.Devinette.tab_score[existe[1]].score += joueur2.score
