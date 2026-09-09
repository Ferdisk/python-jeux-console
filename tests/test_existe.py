"""Tests de la recherche d'un joueur dans les scores enregistrés."""

import Existe


class TestJoueurExiste:
    def test_les_deux_joueurs_sont_connus(self, score_avec_joueurs):
        assert Existe.Joueur_existe("Alice", "Bob", score_avec_joueurs, "Morpion") == [0, 1]

    def test_joueurs_inconnus(self, score_avec_joueurs):
        assert Existe.Joueur_existe("Chloé", "David", score_avec_joueurs, "Morpion") == [-1, -1]

    def test_un_seul_joueur_connu(self, score_avec_joueurs):
        assert Existe.Joueur_existe("Alice", "David", score_avec_joueurs, "Morpion") == [0, -1]

    def test_compte_les_nouveaux_joueurs(self, score_vide):
        Existe.Joueur_existe("Alice", "Bob", score_vide, "Morpion")
        assert score_vide.Morpion.nb_joueur == 2

    def test_ne_compte_pas_les_joueurs_deja_connus(self, score_avec_joueurs):
        avant = score_avec_joueurs.Morpion.nb_joueur
        Existe.Joueur_existe("Alice", "Bob", score_avec_joueurs, "Morpion")
        assert score_avec_joueurs.Morpion.nb_joueur == avant

    def test_chaque_jeu_a_ses_propres_scores(self, score_avec_joueurs):
        """Alice est connue au Morpion mais pas à la Devinette."""
        assert Existe.Joueur_existe("Alice", "Bob", score_avec_joueurs, "Devinette") == [-1, -1]
