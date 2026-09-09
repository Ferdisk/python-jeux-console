import morpion, devinette, Allu, GestionScore

class bcolors:
    """
    Classe contenant des codes ANSI pour styliser le texte dans le terminal.
    Utilisée pour changer la couleur des messages dans la console.

    Attributs :
        GREEN (str) : Code pour le texte vert.
        YELLOW (str) : Code pour le texte jaune.
        RED (str) : Code pour le texte rouge.
        RESET (str) : Code pour réinitialiser le style du texte.
        CYAN (str) : Code pour le texte cyan.
        BG_BLACK (str) : Code pour le fond noir.
    """
    GREEN = "\033[92m"  
    YELLOW = "\033[93m"  
    RED = "\033[91m"  
    RESET = "\033[0m"  
    CYAN = '\033[36m'
    BG_BLACK = '\033[40m'
    
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

def affiche_menu() -> None:
    """Procédure qui affiche le menu des jeux
    """
    print(f"{bcolors.BG_BLACK}Bienvenue dans le menu{bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}Menu des 3 jeux{bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}{bcolors.GREEN}1 Allumette{bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}{bcolors.GREEN}2 Devinette{bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}{bcolors.GREEN}3 Morpion{bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}{bcolors.CYAN}4 Affichage des scores (classés du meilleur au plus mauvais par jeux){bcolors.RESET}")
    print(f"{bcolors.BG_BLACK}{bcolors.RED}5 Quittez{bcolors.RESET}\n")
    


def traitement_menu(j1: str, j2: str, Score_jeux: Score) -> None:
    """Fonction qui traite le choix du menu

    Args:
        j1 (str): nom du joueur 1
        j2 (str): nom du joueur 2
        Score_jeux (Score): Objet de type Score qui contient les scores des joueurs
    """
    choix: int
    quitter: bool
    choix_affichage_scores: int
    choix_jeu: int
    mode: int
    phrase: str

    quitter = False

    # Boucle pour afficher le menu et lancer un jeux tant que l'utilisateur ne quitte pas 
    while not quitter:
        # Affichage du menu 
        affiche_menu()
        # Choix du jeu à lancer ou affichage des scores ou quitter le menu  
        choix = int(input(f"Veuillez choisir un{bcolors.GREEN} jeu (1-3) {bcolors.RESET}, {bcolors.CYAN}afficher les scores (4) {bcolors.RESET}ou{bcolors.RED} quitter (5) {bcolors.RESET}le menu :\n"))
        # Vérification de la validité du choix   
        while choix != 1 and choix != 2 and choix != 3 and choix != 4 and choix != 5:
            choix = int(input(f"{bcolors.RED}Le nombre choisit doit être égal à 1, 2, 3, 4 ou 5{bcolors.RESET}\n"))
        # Choix du mode de jeu
        if choix != 5 and choix != 4: 
            mode = int(input("Veuillez choisir un mode de jeu :\n" 
                                "1 : humain contre humain \n"
                                "2 : humain contre machine \n"
                                "3 : machine contre machine\n\n"))
            # Vérification de la validité du choix du mode de jeu 
            while mode != 1 and mode != 2 and mode != 3:
                mode = int(input("Le nombre choisit doit être égal à 1, 2 ou 3"))
            if mode == 1:
                phrase = "humain contre humain"
            elif mode == 2:
                phrase = "humain contre machine"
            else:
                phrase = "machine contre machine"
        # Lancement du jeu choisi ou affichage des scores ou quitter le menu 
        if choix != 5:
            # Lancement du jeu de l'allumette
            if choix == 1:
                print(f"{bcolors.GREEN}Vous avez choisi le jeu de l'Allumette en mode {phrase}{bcolors.RESET}")
                if mode == 1:
                    Allu.allumettes_humain_vs_humain(j1, j2, Score_jeux)
                elif mode == 2:
                    Allu.allumettes_humain_vs_machine(j1, Score_jeux)  
                else:
                    Allu.allumettes_machine_vs_machine(Score_jeux)
            # Lancement du jeu de la devinette
            elif choix == 2:
                print(f"{bcolors.GREEN}Vous avez choisi le jeu de la Devinette en mode {phrase}{bcolors.RESET}")
                if mode == 1:
                    devinette.devinette_humain_humain(j1, j2, Score_jeux)
                elif mode == 2:
                    devinette.devinette_humain_machine(j1, Score_jeux)  
                else:
                    devinette.devinette_machine_machine()
            # Lancement du jeu du morpion  
            elif choix == 3:
                print(f"{bcolors.GREEN}Vous avez choisi le jeu du Morpion en mode {phrase}{bcolors.RESET}")
                if mode == 1:
                    morpion.morpion_humain_vs_humain(j1, j2, Score_jeux)
                elif mode == 2:
                    morpion.morpion_humain_vs_machine(j1, Score_jeux)
                else:
                    morpion.morpion_machine_vs_machine(Score_jeux)  
            # Affichage des scores 
            elif choix == 4:
                print(f"{bcolors.GREEN}Vous avez choisi d'afficher les scores{bcolors.RESET}")
                choix_affichage_scores = int(input(f"Taper 1 pour afficher les scores de tous les jeux ou 2 pour afficher les scores d'un jeu spécifique :\n"))
                # Vérification de la validité du choix
                while choix_affichage_scores != 1 and choix_affichage_scores != 2:
                    choix_affichage_scores = int(input(f"{bcolors.RED}Le nombre choisit doit être égal à 1 ou 2{bcolors.RESET}\n"))
                if choix_affichage_scores == 2:
                    choix_jeu = int(input(f"Taper 1 pour afficher les scores de l'allumette, 2 pour afficher les scores de la devinette ou 3 pour afficher les scores du morpion :\n"))
                    while choix_jeu != 1 and choix_jeu != 2 and choix_jeu != 3:
                        choix_jeu = int(input(f"{bcolors.RED}Le nombre choisit doit être égal à 1, 2 ou 3{bcolors.RESET}\n"))
                    if choix_jeu == 1:
                        GestionScore.afficher_jeu(Score_jeux.Allumettes, "Allumettes")
                    elif choix_jeu == 2:
                        GestionScore.afficher_jeu(Score_jeux.Devinette, "Devinette")
                    elif choix_jeu == 3:
                        GestionScore.afficher_jeu(Score_jeux.Morpion, "Morpion")
                else:
                    GestionScore.afficher_jeu(Score_jeux.Allumettes, "Allumettes")
                    GestionScore.afficher_jeu(Score_jeux.Devinette, "Devinette")
                    GestionScore.afficher_jeu(Score_jeux.Morpion, "Morpion")
        # Quitter le menu des jeux
        else:
            quitter = True
            print(f"{bcolors.RED}Vous avez quitter le menu des jeux {bcolors.RESET}")

