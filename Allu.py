import Existe 

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


def allumettes(j1: str, j2: str, Score_jeux: Score) -> None:
    """Procédure qui éxécute le jeu des allumettes

    Args:
        j1 (str): chaine de caractère représentant le joueur jouant en premier
        j2 (str): chaine de caractère représentant le joueur jouant en deuxième
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    n: int
    choix: int
    phr_rep: str
    joueur: str
    nb_joueur: int
    test_regle: int
    regle: str
    joueur1: Joueur
    joueur2: Joueur
    existe: list[int]
    

    nb_joueur = 1
    joueur = j1
    phr_rep = "Le gagnant est "
    n = 20
    joueur1 = Joueur()
    joueur2 = Joueur()
    joueur1.nom = j1
    joueur2.nom = j2
    
    # Vérifier si les joueurs existent dans la liste des scores et les ajouter si ce n'est pas le cas
    existe = Existe.Joueur_existe(j1, j2, Score_jeux,"Allumettes")


    # Règles du jeu des allumettes
    regle = (f"{bcolors.MAGENTA}On dispose d'un tas de 20 allumettes. Chaque joueur à tour de rôle peut en prélever 1, 2, 3. Le perdant "
            f"est celui qui prend la dernière allumette{bcolors.RESET}\n")

    # Demander à l'utilisateur s'il a besoin des règles du jeu
    test_regle = int(input("Avez-vous besoin des règles du jeux, répondez positivement par 1 sinon 2:\n"))
    while test_regle != 1 and test_regle != 2:
        test_regle = int(input("Vous devez répondre par 1 (oui) ou 2 (non) : "))

    # Afficher les règles si l'utilisateur en a besoin
    if test_regle == 1:
        print(regle)

    # Boucle principale du jeu qui continue jusqu'à ce qu'il n'y ait plus d'allumettes
    while n > 0:
        # Si le joueur est le joueur 1, afficher un message en jaune
        if joueur == j1:
            print(f"{bcolors.YELLOW}C'est au joueur {nb_joueur} {joueur} {bcolors.RESET}de jouer")
        # Sinon, afficher un message en vert pour le joueur 2
        else:
            print(f"{bcolors.GREEN}C'est au joueur {nb_joueur} {joueur} {bcolors.RESET}de jouer")
        # Afficher le nombre d'allumettes restantes
        print(f"{bcolors.RED}Il reste {n} allumettes {bcolors.RESET}")
        
        # Demander à l'utilisateur de choisir un nombre d'allumettes à retirer (1, 2 ou 3) 
        choix = int(input("Veuillez entrer votre choix égale à 1, 2 ou 3 \n"))
        
        # Boucle pour s'assurer que le choix est valide (1, 2 ou 3)
        while choix != 1 and choix != 2 and choix != 3:
            choix = int(input(f"{bcolors.RED}Votre choix est faux, entrer un choix égale à 1, 2 ou 3{bcolors.RESET}\n"))
        
        # Soustraire le choix du nombre total d'allumettes
        n -= choix
        
        # Si des allumettes restent, changer de joueur
        if n > 0:
            joueur, nb_joueur = (j2, 2) if joueur == j1 else (j1, 1)
    
    # Déterminer le gagnant et mettre à jour les scores
    if nb_joueur == 1: # Si le joueur 1 a pris la dernière allumette, le joueur 2 gagne
        phr_rep = phr_rep + j2
        joueur1.score = 0 
        joueur2.score = 1 
    else: # Sinon, le joueur 1 gagne
        phr_rep = phr_rep + j1
        joueur1.score = 1
        joueur2.score = 0

    # Ajouter les scores des joueurs au tableau des scores du jeu Allumettes
    if existe[0] == -1:
        Score_jeux.Allumettes.tab_score.append(joueur1)
    else:
        Score_jeux.Allumettes.tab_score[existe[0]].score += joueur1.score
    if existe[1] == -1:
        Score_jeux.Allumettes.tab_score.append(joueur2)
    else:
        Score_jeux.Allumettes.tab_score[existe[1]].score += joueur2.score

    # Afficher le résultat final
    print(phr_rep + "\n")



