"""Tests de la logique du Morpion : détection de fin de partie et stratégies."""

import morpion

X, O, V = "X", "O", " "


class TestVerifierVictoire:
    def test_ligne_gagnante(self):
        grille = [[X, X, X], [O, O, V], [V, V, V]]
        assert morpion.verifier_victoire(grille, X) is True

    def test_colonne_gagnante(self):
        grille = [[X, O, V], [X, O, V], [X, V, V]]
        assert morpion.verifier_victoire(grille, X) is True

    def test_diagonale_descendante(self):
        grille = [[X, O, V], [O, X, V], [V, V, X]]
        assert morpion.verifier_victoire(grille, X) is True

    def test_diagonale_montante(self):
        grille = [[V, O, X], [O, X, V], [X, V, V]]
        assert morpion.verifier_victoire(grille, X) is True

    def test_pas_de_victoire(self):
        grille = [[X, O, X], [O, V, V], [V, V, V]]
        assert morpion.verifier_victoire(grille, X) is False

    def test_ne_confond_pas_les_symboles(self):
        """Une ligne de X ne doit pas faire gagner O."""
        grille = [[X, X, X], [V, V, V], [V, V, V]]
        assert morpion.verifier_victoire(grille, O) is False


class TestEstMatchNul:
    def test_grille_pleine(self):
        grille = [[X, O, X], [X, O, O], [O, X, X]]
        assert morpion.est_match_nul(grille) is True

    def test_grille_incomplete(self, grille_vide):
        grille_vide[1][1] = X
        assert morpion.est_match_nul(grille_vide) is False

    def test_grille_vide(self, grille_vide):
        assert morpion.est_match_nul(grille_vide) is False


class TestMinimax:
    """Le score renvoyé est 1 si le premier symbole gagne, -1 s'il perd, 0 en cas de nul."""

    def test_victoire_du_maximisant(self):
        grille = [[X, X, X], [O, O, V], [V, V, V]]
        assert morpion.minimax(grille, 0, False, [X, O]) == 1

    def test_victoire_du_minimisant(self):
        grille = [[O, O, O], [X, X, V], [V, V, V]]
        assert morpion.minimax(grille, 0, True, [X, O]) == -1

    def test_grille_pleine_sans_gagnant(self):
        grille = [[X, O, X], [X, O, O], [O, X, X]]
        assert morpion.minimax(grille, 0, True, [X, O]) == 0

    def test_victoire_forcee_detectee(self):
        """X joue et dispose d'un alignement imparable : minimax doit annoncer 1."""
        grille = [[X, X, V], [O, O, V], [V, V, V]]
        assert morpion.minimax(grille, 0, True, [X, O]) == 1


class TestCoupMachineDifficile:
    def test_prend_la_victoire_immediate(self):
        grille = [[X, X, V], [O, O, V], [V, V, V]]
        assert morpion.coup_machine_difficile(grille, [X, O]) == (0, 2)

    def test_ne_modifie_pas_la_grille(self):
        grille = [[X, X, V], [O, O, V], [V, V, V]]
        avant = [ligne[:] for ligne in grille]
        morpion.coup_machine_difficile(grille, [X, O])
        assert grille == avant


class TestCoupMachineMoyen:
    def test_prefere_gagner_plutot_que_bloquer(self):
        """O peut gagner en (0,2) et bloquer en (1,2) : il doit choisir la victoire."""
        grille = [[O, O, V], [X, X, V], [V, V, V]]
        assert morpion.coup_machine_moyen(grille, O) == (0, 2)

    def test_bloque_une_menace(self):
        grille = [[X, X, V], [O, V, V], [V, V, V]]
        assert morpion.coup_machine_moyen(grille, O) == (0, 2)

    def test_joue_une_case_vide_sans_menace(self, grille_vide):
        ligne, colonne = morpion.coup_machine_moyen(grille_vide, O)
        assert grille_vide[ligne][colonne] == V

    def test_ne_modifie_pas_la_grille(self):
        grille = [[X, X, V], [O, V, V], [V, V, V]]
        avant = [ligne[:] for ligne in grille]
        morpion.coup_machine_moyen(grille, O)
        assert grille == avant


class TestCoupMachineFacile:
    def test_joue_toujours_une_case_vide(self, grille_vide):
        grille_vide[0][0] = X
        grille_vide[1][1] = O
        for _ in range(50):
            ligne, colonne = morpion.coup_machine_facile(grille_vide)
            assert grille_vide[ligne][colonne] == V
