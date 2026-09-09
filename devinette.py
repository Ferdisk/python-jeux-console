import Existe, getpass, random

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


def devinette_humain_humain(j1: str, j2: str, Score_jeux: Score) -> None:
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


def coup_facile(borne_inf: int, borne_sup: int) -> int:
    """
    Fonction qui retourne un coup aléatoire pour la machine en mode facile.

    Args:
        borne_inf (int): Borne inférieure de l'intervalle.
        borne_sup (int): Borne supérieure de l'intervalle.

    Returns:
        int: Un nombre aléatoire entre borne_inf et borne_sup.
    """
    return random.randint(borne_inf, borne_sup)

def coup_moyen(borne_inf: int, borne_sup: int) -> int:
    """
    Fonction qui retourne un coup pour la machine en mode moyen (recherche binaire).

    Args:
        borne_inf (int): Borne inférieure de l'intervalle.
        borne_sup (int): Borne supérieure de l'intervalle.

    Returns:
        int: Le nombre au milieu de l'intervalle.
    """
    return (borne_inf + borne_sup) // 2

def coup_difficile(borne_inf: int, borne_sup: int) -> int:
    """
    Fonction qui retourne un coup pour la machine en mode difficile (hybride).

    Args:
        borne_inf (int): Borne inférieure de l'intervalle.
        borne_sup (int): Borne supérieure de l'intervalle.

    Returns:
        int: Un nombre choisi avec une stratégie hybride.
    """
    if random.random() < 0.80:  # 80% de chances d'utiliser la recherche binaire
        return (borne_inf + borne_sup) // 2
    else:  # 20% de chances de choisir un nombre aléatoire
        return random.randint(borne_inf, borne_sup)


def devinette_humain_machine(j1: str, Score_jeux: Score) -> None:
    """
    Procédure qui exécute le jeu de la devinette en mode humain contre machine.

    Args:
        j1 (str): Nom du joueur humain.
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs.
    """
    limite: int
    reponse: int
    tour: int 
    tour = 1
    choix: int
    trouver: bool 
    trouver= False
    test_regle: int
    regle: str
    j2: str 
    j2= "Machine"
    score_j1: int 
    score_j1 = 0
    score_j2: int 
    score_j2 = 10
    existe: list[int]
    mode: int

    # Vérification de l'existence des joueurs dans la liste des scores
    existe = Existe.Joueur_existe(j1, j2, Score_jeux, "Devinette")

    # Choix du mode de jeu
    mode = int(input("Veuillez choisir un mode de jeu :\n"
                     "1 : mode facile \n"
                     "2 : mode moyen \n"
                     "3 : mode difficile \n\n"))
    
    # Vérification de la validité du choix du mode de jeu
    while mode != 1 and mode != 2 and mode != 3:
        mode = int(input("Le nombre choisi doit être égal à 1, 2 ou 3 : "))

    # Règles du jeu de la devinette
    regle = (f"{bcolors.MAGENTA}Le joueur 1 (humain) choisit un nombre entre 1 et une limite. "
             f"La machine doit deviner ce nombre : à chacune de ses propositions, le joueur répond 'trop petit', "
             f"'trop grand', ou 'c'est gagné'.{bcolors.RESET}\n")

    # Demande si le joueur a besoin des règles du jeu
    test_regle = int(input("Avez-vous besoin des règles du jeu, répondez positivement par 1 sinon 2:\n"))
    while test_regle != 1 and test_regle != 2:
        test_regle = int(input("Vous devez répondre positivement par 1 sinon 2 : \n"))

    # Affichage des règles du jeu si besoin
    if test_regle == 1:
        print(regle)

    # Demande de la limite du nombre à deviner
    limite = int(input(f"{bcolors.YELLOW}Joueur 1 {j1}{bcolors.RESET} : Veuillez choisir la limite : \n"))
    while limite <= 1:
        limite = int(input(f"{bcolors.RED}Votre limite doit être un nombre positif strictement supérieur à 1 : \n{bcolors.RESET}"))

    # Le joueur humain choisit un nombre à deviner
    reponse = int(getpass.getpass(f"{bcolors.GREEN}Joueur 1 {j1}{bcolors.RESET} : Choisissez le nombre à deviner (entre 1 et {limite}) : \n"))
    while reponse < 1 or reponse > limite:
        print(f"{bcolors.RED}Vous devez choisir un nombre entre 1 et {limite}{bcolors.RESET}")
        reponse = int(getpass.getpass(f"{bcolors.GREEN}Joueur 1 {j1}{bcolors.RESET} : Choisissez le nombre à deviner : \n"))

    # Initialisation des bornes pour la recherche binaire
    borne_inf: int 
    borne_inf = 1
    borne_sup: int 
    borne_sup = limite

    # Boucle principale du jeu
    while not trouver:
        print(f"{bcolors.GREEN}Tour {tour} : Machine {j2} essaie de deviner.{bcolors.RESET}")

        # La machine choisit un coup en fonction de la difficulté
        if mode == 1:
            choix = coup_facile(borne_inf, borne_sup)
        elif mode == 2:
            choix = coup_moyen(borne_inf, borne_sup)
        else:  # mode difficile
            choix = coup_difficile(borne_inf, borne_sup)

        print(f"La machine propose : {choix}")

        if choix < reponse:
            print(f"{bcolors.RED}Trop petit{bcolors.RESET}\n")
            borne_inf = choix + 1  # On met à jour la borne inférieure
            score_j1 += 1
            score_j2 -= 1
        elif choix > reponse:
            print(f"{bcolors.RED}Trop grand{bcolors.RESET}\n")
            borne_sup = choix - 1  # On met à jour la borne supérieure
            score_j1 += 1
            score_j2 -= 1
        else:
            print(f"{bcolors.YELLOW}C'est gagné ! Le nombre était {reponse}.{bcolors.RESET}")
            print(f"{bcolors.GREEN}Score final : {j1} a {score_j1} points, {j2} a {score_j2} points.{bcolors.RESET}")
            trouver = True

        tour += 1

    # Mise à jour des scores dans Score_jeux
    joueur1 = Joueur()
    joueur2 = Joueur()
    joueur1.nom = j1
    joueur2.nom = j2
    joueur1.score = score_j1
    joueur2.score = score_j2

    if existe[0] == -1:
        Score_jeux.Devinette.tab_score.append(joueur1)
    else:
        Score_jeux.Devinette.tab_score[existe[0]].score += joueur1.score

    if existe[1] == -1:
        Score_jeux.Devinette.tab_score.append(joueur2)
    else:
        Score_jeux.Devinette.tab_score[existe[1]].score += joueur2.score

def devinette_machine_machine() -> None:
    """
    Procédure qui exécute le jeu de la devinette en mode machine contre machine.
    """
    limite: int
    reponse: int
    tour: int = 1
    choix: int
    trouver: bool 
    trouver = False
    mode: int

    # Choix du mode de jeu
    mode = int(input("Veuillez choisir un mode de jeu :\n"
                     "1 : mode facile \n"
                     "2 : mode moyen \n"
                     "3 : mode difficile \n\n"))
    
    # Vérification de la validité du choix du mode de jeu
    while mode != 1 and mode != 2 and mode != 3:
        mode = int(input("Le nombre choisi doit être égal à 1, 2 ou 3 : "))

    # La Machine 1 choisit une limite aléatoire
    limite = random.randint(10, 100)
    print(f"{bcolors.YELLOW}Machine 1 a choisi une limite de {limite}.{bcolors.RESET}")

    # La Machine 1 choisit un nombre aléatoire entre 1 et la limite
    reponse = random.randint(1, limite)
    print(f"{bcolors.YELLOW}Machine 1 a choisi un nombre entre 1 et {limite}.{bcolors.RESET}")

    # Initialisation des bornes pour la recherche binaire
    borne_inf: int 
    borne_inf = 1
    borne_sup: int 
    borne_sup = limite

    # Boucle principale du jeu
    while not trouver:
        print(f"{bcolors.GREEN}Tour {tour} : Machine 2 essaie de deviner.{bcolors.RESET}")

        # La machine choisit un coup en fonction de la difficulté
        if mode == 1:
            choix = coup_facile(borne_inf, borne_sup)
        elif mode == 2:
            choix = coup_moyen(borne_inf, borne_sup)
        else:  # mode difficile
            choix = coup_difficile(borne_inf, borne_sup)

        print(f"Machine 2 propose : {choix}")

        if choix < reponse:
            print(f"{bcolors.RED}Trop petit{bcolors.RESET}\n")
            borne_inf = choix + 1  # On met à jour la borne inférieure
        elif choix > reponse:
            print(f"{bcolors.RED}Trop grand{bcolors.RESET}\n")
            borne_sup = choix - 1  # On met à jour la borne supérieure
        else:
            print(f"{bcolors.YELLOW}C'est gagné ! Le nombre était {reponse}.{bcolors.RESET}")
            print(f"{bcolors.GREEN}Machine 2 a trouvé le nombre en {tour} tentatives.{bcolors.RESET}")
            trouver = True

        tour += 1