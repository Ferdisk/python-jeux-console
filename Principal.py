import Menu, GestionScore

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


if __name__ == "__main__":
    j1: str
    j2: str
    Score_jeux: Score
    scores: list[Score]

    # Désérialiser le fichier pour obtenir les données existantes
    filePath = "scores.bin"
    scores = GestionScore.load_scores(filePath)

    # Créer une instance de la classe Score pour les jeux à venir 
    Score_jeux = Score()
    Score_jeux.Devinette = Jeux()
    Score_jeux.Morpion = Jeux()
    Score_jeux.Allumettes = Jeux()
    Score_jeux.Devinette.tab_score = []
    Score_jeux.Morpion.tab_score = []
    Score_jeux.Allumettes.tab_score = []
    Score_jeux.Devinette.nb_joueur = 0
    Score_jeux.Morpion.nb_joueur = 0
    Score_jeux.Allumettes.nb_joueur = 0
    
    # Si des données existent, les charger dans les variables appropriées pour les utiliser dans le programme  
    if scores:
        Score_jeux = scores[0]

    # Demander les noms des joueurs pour les jeux à venir et les afficher dans le menu principal 
    j1 = input(f"Qui est le {bcolors.YELLOW}joueur 1{bcolors.RESET}\n")
    j2 = input(f"Qui est le {bcolors.GREEN}joueur 2{bcolors.RESET}\n")
    print("")
    # Traiter le menu principal pour les jeux à venir 
    Menu.traitement_menu(j1, j2, Score_jeux)
    
    # Mettre à jour les scores avec les nouvelles informations
    scores = [Score_jeux]

    # Sérialiser les données mises à jour dans le fichier
    GestionScore.save_scores(filePath, scores)