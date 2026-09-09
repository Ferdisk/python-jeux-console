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

def Joueur_existe(j1: str, j2: str, Score_jeux: Score, jeu: str) -> list[int]:
    """Procédure qui vérifie si les joueurs existent dans la liste des scores et les ajoute 
    si ce n'est et retourne un tableau contenant l'indice des joueurs dans la liste des scores s'ils existent, -1 sinon 

    Args:
        j1 (str): nom du joueur 1
        j2 (str): nom du joueur 2
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
        jeu (str): nom du jeu
    
    Returns:
        list[int]: Liste contenant l'indice des joueurs dans la liste des scores s'ils existent, -1 sinon"""
    compteur: int
    est_trouve_j1: bool
    est_trouve_j2: bool
    tab_score: list[Joueur]
    joueur: Joueur
    resultat: list[int]
    
    tab_score = []
    compteur = 0
    est_trouve_j1 = False
    est_trouve_j2 = False
    resultat = [-1, -1]
    
    # Sélection de la liste tab_score appropriée en fonction du jeu
    if jeu == 'Devinette':
        tab_score = Score_jeux.Devinette.tab_score
    elif jeu == 'Morpion':
        tab_score = Score_jeux.Morpion.tab_score
    elif jeu == 'Allumettes':
        tab_score = Score_jeux.Allumettes.tab_score
  

    # Utilisation d'une boucle while pour vérifier si les joueurs existent
    while compteur < len(tab_score) and not (est_trouve_j1 and est_trouve_j2):
        joueur = tab_score[compteur]
        if joueur.nom == j1:
            est_trouve_j1 = True
            resultat[0] = compteur
        elif joueur.nom == j2:
            est_trouve_j2 = True
            resultat[1] = compteur
        compteur += 1

    # Mise à jour du nombre de joueurs si les joueurs ne sont pas trouvés
    if not est_trouve_j1:
        if jeu == 'Devinette':
            Score_jeux.Devinette.nb_joueur += 1
        elif jeu == 'Morpion':
            Score_jeux.Morpion.nb_joueur += 1
        elif jeu == 'Allumettes':
            Score_jeux.Allumettes.nb_joueur += 1

    if not est_trouve_j2:
        if jeu == 'Devinette':
            Score_jeux.Devinette.nb_joueur += 1
        elif jeu == 'Morpion':
            Score_jeux.Morpion.nb_joueur += 1
        elif jeu == 'Allumettes':
            Score_jeux.Allumettes.nb_joueur += 1
    
    return resultat