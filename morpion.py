import Existe, math, random, time
from typing import List

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

deb = time.time()
def afficher_grille(tab: List[List[str]]) -> None:
    """Procédure qui affiche la grille du morpion

    Args:
        tab (List[List[str]]): une liste de listes de chaines de caractère
    """
    i: int

    for i in range(3):
        # Affiche chaque case de la ligne avec un séparateur "|"
        print(tab[i][0], "|", tab[i][1], "|", tab[i][2])
        # Si ce n'est pas la dernière ligne, affiche une ligne de séparation
        if i < 2:
            print("-" * 9)


def verifier_victoire(tab: List[List[str]], symbole: str) -> bool:
    """Fonction qui vérifie si un joueur a gagné

    Args:
        tab (List[List[str]]): une liste de listes de chaines de caractère
        symbole (str): chaine de caractère représentant le symbole du joueur

    Returns:
        bool: Un booléen pour savoir si un joueur a gagné ou non (True pour gagné, False pour non gagné)  
    """
    ligne: List[str]
    col: int

    for ligne in tab:  # Vérifie si les lignes ont le même symboles
        if ligne == [symbole, symbole, symbole]:
            return True
    for col in range(3):  # Vérifie si les colonnes ont le même symboles
        if tab[0][col] == symbole and tab[1][col] == symbole and tab[2][col] == symbole:
            return True
    if tab[0][0] == symbole and tab[1][1] == symbole and tab[2][2] == symbole:  # Vérifie si les symboles de la
        # diagonale de la droite vers gauche sont les mêmes
        return True
    if tab[0][2] == symbole and tab[1][1] == symbole and tab[2][0] == symbole:  # Vérifie si les symboles de la
        # diagonale de la gauche vers la droite sont les mêmes
        return True
    return False


def est_match_nul(tab: List[List[str]]) -> bool:
    """Fonction qui vérifie si la grille est pleine (match nul)

    Args:
        tab (List[List[str]]): une liste de listes de chaines de caractère

    Returns:
        bool: Un booléen pour savoir si la grille est pleine ou non (True pour pleine, False pour non pleine)
    """
    ligne: List[str]
    case: str

    # Vérifie s'il reste des cases vides
    for ligne in tab:
        for case in ligne:
            if case == " ":
                return False  # Il reste des cases vides, donc pas de match nul
    return True  # Aucune case vide, donc match nul

def coup_machine_difficile(tab: List[List[str]], liste_symbole: list[str]) -> tuple[int, int]:
    """Fonction qui retourne le meilleur coup pour la machine en mode difficile

    Args:
        tab (List[List[str]]): une liste de listes de chaines de caractère
        liste_symbole (list[str]): une liste de deux chaines de caractère représentant les symboles des joueurs

    Returns:
        tuple[int, int]: un tuple contenant les indices de la ligne et de la colonne du meilleur coup
    """
    meilleur_coup: tuple[int, int]
    meilleur_score: float
    score: float

    meilleur_score = -math.inf
    meilleur_coup = None
    for i in range(3):
        for j in range(3):
            if tab[i][j] == " ":
                tab[i][j] = liste_symbole[0]
                score = minimax(tab, 0, False, liste_symbole)
                tab[i][j] = " "
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (i, j)
    return meilleur_coup

def minimax(tab: List[List[str]], profondeur: int, est_maximisant: bool, liste_symbole: list[str]) -> int:
    """Fonction qui implémente l'algorithme minimax pour le jeu du morpion

    Args:
        tab (List[List[str]]): une liste de listes de chaines de caractère
        profondeur (int):  #TODO: décrire ce paramètre
        est_maximisant (bool): un booléen pour savoir si on maximise ou minimise le score
        liste_symbole ([str, str]): une liste de deux chaines de caractère représentant les symboles des joueurs

    Returns:
        int: #TODO: décrire ce que retourne la fonction
    """
    if verifier_victoire(tab, liste_symbole[0]):
        return 1
    if verifier_victoire(tab, liste_symbole[1]):
        return -1
    if est_match_nul(tab):
        return 0
    
    if est_maximisant:
        meilleur_score = -math.inf
        for i in range(3):
            for j in range(3):
                if tab[i][j] == " ":
                    tab[i][j] = liste_symbole[0]
                    score = minimax(tab, profondeur + 1, False, liste_symbole)
                    tab[i][j] = " "
                    meilleur_score = max(score, meilleur_score)
        return meilleur_score
    else:
        meilleur_score = math.inf
        for i in range(3):
            for j in range(3):
                if tab[i][j] == " ":
                    tab[i][j] = liste_symbole[1]
                    score = minimax(tab, profondeur + 1, True, liste_symbole)
                    tab[i][j] = " "
                    meilleur_score = min(score, meilleur_score)
        return meilleur_score

def morpion_humain_vs_humain(j1: str, j2: str, Score_jeux: Score) -> None:
    """Procédure qui éxécute le jeu du morpion

    Args:
        j1 (str): nom du joueur 1
        j2 (str): nom du joueur 2
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    test_regle: int
    regle: str
    joueur1: Joueur
    joueur2: Joueur
    joueur: str
    symbole: str
    jeu_termine: bool
    tab: List[List[str]]
    i: int
    existe: list[int]

    tab = [[" ", " ", " "] for i in range(3)]
    
    joueur1 = Joueur()
    joueur2 = Joueur()
    joueur1.nom = j1
    joueur2.nom = j2
    joueur1.score = 0
    joueur2.score = 0

    # Vérifier si les joueurs existent dans la liste des scores et les ajouter si ce n'est pas le cas
    existe = Existe.Joueur_existe(j1, j2, Score_jeux, "Morpion")

    # Règles du jeu du morpion 
    regle = (f"{bcolors.MAGENTA}Chaque joueur pose sa marque (un O ou une X) à tour de rôle dans les cases d'une grille de 3x3. Le "
             f"premier qui aligne 3 marques a gagné{bcolors.RESET}\n")

    # Demande si le joueur a besoin des règles du jeu 
    test_regle = int(input("Avez-vous besoin des règles du jeux, répondez positivement par 1 sinon 2:\n"))
    # Vérification de la validité de la réponse  
    while test_regle != 1 and test_regle != 2:
        test_regle = int(input(f"{bcolors.RED}Vous devez répondre positivement par 1 sinon 2: \n{bcolors.RESET}"))

    # Affichage des règles du jeu si besoin
    if test_regle == 1:
        print(regle)
    afficher_grille(tab)

    joueur = j1
    symbole = "X"
    jeu_termine = False  # Variable pour contrôler l'état du jeu

    # Boucle principale du jeu qui continue tant que le jeu n'est pas terminé 
    while not jeu_termine:
        # Affiche le joueur et son symbole
        print(f"{bcolors.RED}Tour de {joueur} ({symbole}) {bcolors.RESET}")
        # Demande à l'utilisateur de choisir une ligne 
        ligne = int(input("Choisissez une ligne (1, 2 ou 3) : "))
        # Vérification de la validité de la ligne choisie 
        while ligne != 1 and ligne != 2 and ligne != 3:
            ligne = int(input(f"{bcolors.RED}La ligne doit être égal à 1, 2 ou 3 : {bcolors.RESET}"))
        # Demande à l'utilisateur de choisir une colonne
        colonne = int(input("Choisissez une colonne (1, 2 ou 3) : "))
        # Vérification de la validité de la colonne choisie
        while colonne != 1 and colonne != 2 and colonne != 3:
            colonne = int(input(f"{bcolors.RED}La colonne doit être égal à 1, 2 ou 3 : {bcolors.RESET}"))
        # On décrémente les valeurs pour correspondre aux indices de la liste (qui commence à 0)
        ligne -= 1
        colonne -= 1

        # Vérification de la disponibilité de la case choisie (si elle est vide)
        if tab[ligne][colonne] == " ":
            # Mettre le symbole du joueur dans la case choisie qui est vide
            tab[ligne][colonne] = symbole
            afficher_grille(tab)
            # Vérification si un joueur a gagné
            if verifier_victoire(tab, symbole):
                print(f"{bcolors.YELLOW}{joueur} a gagné !{bcolors.RESET}\n")
                jeu_termine = True  
                # Incrémente le score du joueur gagnant
                if joueur == j1:
                    joueur1.score += 1
                else:
                    joueur2.score += 1
            # Vérification si la grille est pleine (match nul)
            elif est_match_nul(tab):
                print(f"{bcolors.GREEN} Match nul ! {bcolors.RESET}\n")
                jeu_termine = True  
            # Sinon, le jeu continue tant que la grille n'est pas pleine ou qu'un joueur n'a pas gagné
            else:
                # Alterne les joueurs si le jeu continue
                joueur, symbole = (j2, "O") if joueur == j1 else (j1, "X")
        # Si la case choisie est déjà prise, affiche un message d'erreur
        else:
            print(f"{bcolors.RED}Case déjà prise, choisissez une autre case.{bcolors.RESET}")

    # Mettre à jour les scores des joueurs
    if existe[0] == -1:
        Score_jeux.Morpion.tab_score.append(joueur1)
    else:
        Score_jeux.Morpion.tab_score[existe[0]].score += joueur1.score
    if existe[1] == -1:
        Score_jeux.Morpion.tab_score.append(joueur2)
    else:
        Score_jeux.Morpion.tab_score[existe[1]].score += joueur2.score

def morpion_humain_vs_machine(j1: str, Score_jeux: Score) -> None:
    """Procédure qui éxécute le jeu du morpion en mode humain contre la machine

    Args:
        j1 (str): nom du joueur 1
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    tab = [[" ", " ", " "] for _ in range(3)]
    joueur = Joueur()
    joueur.nom = j1
    joueur.score = 0

    liste_symbole = ["O", "X"]

    # Choix du niveau de difficulté
    difficulte = input("Choisissez le niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile): ")
    while difficulte not in ["1", "2", "3"]:
        difficulte = input(f"{bcolors.RED}Veuillez choisir 1, 2 ou 3: {bcolors.RESET}")

    jeu_termine = False
    tour_joueur = True

    while not jeu_termine:
        afficher_grille(tab)
        
        if tour_joueur:
            # Tour du joueur humain (code existant)
            print(f"{bcolors.RED}Tour de {joueur.nom} (X) {bcolors.RESET}")
            ligne = int(input("Choisissez une ligne (1, 2 ou 3) : ")) 
            while ligne != 1 and ligne != 2 and ligne != 3:
                ligne = int(input(f"{bcolors.RED}La ligne doit être égal à 1, 2 ou 3 : {bcolors.RESET}"))
            ligne -= 1
            colonne = int(input("Choisissez une colonne (1, 2 ou 3) : ")) 
            while colonne != 1 and colonne != 2 and colonne != 3:
                colonne = int(input(f"{bcolors.RED}La colonne doit être égal à 1, 2 ou 3 : {bcolors.RESET}"))
            colonne -= 1
            
            if tab[ligne][colonne] == " ":
                tab[ligne][colonne] = "X"
                if verifier_victoire(tab, "X"):
                    print(f"{bcolors.YELLOW}{joueur.nom} a gagné !{bcolors.RESET}")
                    joueur.score += 1
                    jeu_termine = True
                elif est_match_nul(tab):
                    print(f"{bcolors.GREEN}Match nul !{bcolors.RESET}")
                    jeu_termine = True
                tour_joueur = False
            else:
                print(f"{bcolors.RED}Case déjà prise, choisissez une autre case.{bcolors.RESET}")
        else:
            # Tour de la machine
            print(f"{bcolors.RED}Tour de la machine (O) {bcolors.RESET}")
            if difficulte == "1":
                coup = coup_machine_facile(tab) 
            elif difficulte == "2":
                coup = coup_machine_moyen(tab, "O") 
            else:
                coup = coup_machine_difficile(tab, liste_symbole)
            
            tab[coup[0]][coup[1]] = "O"
            if verifier_victoire(tab, "O"):
                print(f"{bcolors.YELLOW}La machine a gagné !{bcolors.RESET}")
                jeu_termine = True
            elif est_match_nul(tab):
                print(f"{bcolors.GREEN}Match nul !{bcolors.RESET}")
                jeu_termine = True
            tour_joueur = True

    # Mise à jour du score
    existe = Existe.Joueur_existe(j1, "Machine", Score_jeux, "Morpion")
    if existe[0] == -1:
        Score_jeux.Morpion.tab_score.append(joueur)
    else:
        Score_jeux.Morpion.tab_score[existe[0]].score += joueur.score

def morpion_machine_vs_machine(Score_jeux: Score) -> None:
    """Procédure qui éxécute le jeu du morpion en mode machine contre la machine

    Args:
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    tab = [[" ", " ", " "] for _ in range(3)]
    joueur1 = Joueur()
    joueur1.nom = "Bot 1"
    joueur1.score = 0
    joueur2 = Joueur()
    joueur2.nom = "Bot 2"
    joueur2.score = 0

    liste_symbole = ["X", "O"]

    # Choix du niveau de difficulté
    difficulte = input("Choisissez le niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile): ")
    while difficulte not in ["1", "2", "3"]:
        difficulte = input(f"{bcolors.RED}Veuillez choisir 1, 2 ou 3: {bcolors.RESET}")

    jeu_termine = False
    joueur = "Bot 1"

    while not jeu_termine:
        afficher_grille(tab)
        
        # Tour de la machine
        print(f"{bcolors.RED}Tour de {joueur} {liste_symbole[0]} {bcolors.RESET}")
        if difficulte == "1":
            coup = coup_machine_facile(tab) # TODO: Implémenter la fonction coup_machine_facile
        elif difficulte == "2":
            coup = coup_machine_moyen(tab, liste_symbole[0]) # TODO: Implémenter la fonction coup_machine_moyen
        else:
            coup = coup_machine_difficile(tab, liste_symbole)
        
        tab[coup[0]][coup[1]] = liste_symbole[0]
        if verifier_victoire(tab, liste_symbole[0]):
            print(f"{bcolors.YELLOW}La machine a gagné !{bcolors.RESET}")
            jeu_termine = True
        elif est_match_nul(tab):
            print(f"{bcolors.GREEN}Match nul !{bcolors.RESET}")
            jeu_termine = True
        else:
            joueur, liste_symbole = ("Bot 2", ["O", "X"]) if joueur == "Bot 1" else ("Bot 1", ["X", "O"])

    # Mise à jour du score
    existe = Existe.Joueur_existe(joueur1.nom, joueur2.nom, Score_jeux, "Morpion")
    if existe[0] == -1:
        Score_jeux.Morpion.tab_score.append(joueur1)
    else:
        Score_jeux.Morpion.tab_score[existe[0]].score += joueur1.score
    if existe[1] == -1:
        Score_jeux.Morpion.tab_score.append(joueur2)
    else:
        Score_jeux.Morpion.tab_score[existe[1]].score += joueur2.score

def coup_machine_facile(tab: List[List[str]]) -> tuple[int, int]:
    """
    Fonction qui retourne un coup aléatoire pour la machine en mode facile.

    Args:
        tab (List[List[str]]): La grille du Morpion.

    Returns:
        Tuple[int, int]: Les coordonnées (ligne, colonne) du coup choisi.
    """
    cases_vides = [(i, j) for i in range(3) for j in range(3) if tab[i][j] == " "]
    return random.choice(cases_vides)



def coup_machine_moyen(tab: List[List[str]], symbole: str) -> tuple[int, int]:
    """
    Fonction qui retourne un coup pour la machine en mode moyen.
    La machine essaie de gagner si possible, sinon essaie de bloquer le joueur humain, et sinon joue de manière aléatoire.

    Args:
        tab (List[List[str]]): La grille du Morpion.
        symbole (str): Le symbole de la machine (O).

    Returns:
        Tuple[int, int]: Les coordonnées (ligne, colonne) du coup choisi.
    """
    # Vérifier si la machine peut gagner au prochain coup
    for i in range(3):
        for j in range(3):
            if tab[i][j] == " ":  # Case vide
                tab[i][j] = symbole  # Simuler le coup
                if verifier_victoire(tab, symbole):  # Vérifier si la machine gagne
                    tab[i][j] = " "  # Annuler le coup simulé
                    return (i, j)
                tab[i][j] = " "  # Annuler le coup simulé

    # Vérifier si le joueur humain peut gagner au prochain coup et le bloquer
    symbole_joueur = "X" if symbole == "O" else "O"
    for i in range(3):
        for j in range(3):
            if tab[i][j] == " ":  # Case vide
                tab[i][j] = symbole_joueur  # Simuler le coup du joueur
                if verifier_victoire(tab, symbole_joueur):  # Vérifier si le joueur gagne
                    tab[i][j] = " "  # Annuler le coup simulé
                    return (i, j)  # Bloquer le joueur
                tab[i][j] = " "  # Annuler le coup simulé

    # Si aucun coup gagnant ou bloquant, jouer de manière aléatoire
    return coup_machine_facile(tab)
fin = time.time()
print(f"Temps d'exécution : {fin - deb} secondes")


