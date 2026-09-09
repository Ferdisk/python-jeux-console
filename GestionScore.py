import pickle

class bcolors:
    """
    Classe contenant des codes ANSI pour styliser le texte dans le terminal.
    Utilisée pour changer la couleur des messages dans la console.

    Attributs :
        GREEN (str) : Code pour le texte vert.
        YELLOW (str) : Code pour le texte jaune.
        RED (str) : Code pour le texte rouge.
        RESET (str) : Code pour réinitialiser le style du texte.
    """
    GREEN = "\033[92m"  
    YELLOW = "\033[93m"  
    RED = "\033[91m"  
    RESET = "\033[0m" 

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


def checkFileExistance(filePath: str)-> bool:
    """Fonction qui vérifie si un fichier existe.

    Args:
        filePath (str): Chemin du fichier

    Returns:
        bool: True si le fichier existe, False sinon
    """
    try:
        with open(filePath, 'r'):
            return True
    except FileNotFoundError:
        return False


def load_scores(filePath: str) -> list[Joueur]:
    """Fonction qui charge les scores à partir d'un fichier binaire.

    Args:
        filePath (str): Chemin du fichier binaire

    Returns:
        list[Joueur]: Liste des scores chargés à partir du fichier binaire ou une liste vide si le fichier n'existe pas ou est vide  
    """
    try:
        with open(filePath, 'rb') as file:
            return pickle.load(file)
    except (EOFError, FileNotFoundError):
        return []

def save_scores(filePath: str, scores: list[Joueur]) -> None:
    """Procédure qui sauvegarde les scores dans un fichier binaire.

    Args:
        filePath (str): Chemin du fichier binaire 
        scores (list[Joueur]): Liste des scores à sauvegarder
    """
    with open(filePath, 'wb') as file:
        pickle.dump(scores, file)

def importScore(filePath: str, Score_jeux: Score) -> None:
    """Procédure qui importe les scores à partir d'un fichier binaire.

    Args:
        filePath (str): Chemin du fichier binaire
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    scores: list[Score]
    if not checkFileExistance(filePath):  # teste si le fichier n'existe pas
        with open(filePath, 'wb') as file:  # créer un fichier binaire vide
            pickle.dump([Score_jeux], file)  # Écrire une liste contenant Score_jeux
    else:
        # Lire les données existantes
        with open(filePath, 'rb') as file:
            try:
                scores = pickle.load(file)
            except EOFError:
                scores = []
        
        # Mettre à jour les données avec Score_jeux
        updated = False
        for i in range(len(scores)):
            if (scores[i].Devinette.nb_joueur == Score_jeux.Devinette.nb_joueur and
                scores[i].Morpion.nb_joueur == Score_jeux.Morpion.nb_joueur and
                scores[i].Allumettes.nb_joueur == Score_jeux.Allumettes.nb_joueur):
                scores[i] = Score_jeux
                updated = True

        if not updated:
            scores.append(Score_jeux)

        # Réécrire le fichier avec les données mises à jour
        with open(filePath, 'wb') as file:
            pickle.dump(scores, file)

       
def afficher_jeu(jeu: Jeux, nom_jeu: str):
    print(f"{bcolors.YELLOW}{nom_jeu}{bcolors.RESET}\n")
    # Créer une copie de la liste des joueurs pour éviter de modifier l'originale
    joueurs = list(jeu.tab_score)

    # Implémentation d'un algorithme tri à bulles pour trier les scores
    n = len(joueurs)
    for i in range(n):
        for j in range(0, n-i-1):
            if joueurs[j].score < joueurs[j+1].score:
                joueurs[j], joueurs[j+1] = joueurs[j+1], joueurs[j]
    
    # Afficher les joueurs triés
    for joueur in joueurs:
        print(f"{bcolors.GREEN}{joueur.nom: <20s} {joueur.score: >4d}{bcolors.RESET}")
    print("")

   


