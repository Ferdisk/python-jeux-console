"""Tests de la persistance des scores.

Tous les tests écrivent dans le répertoire temporaire fourni par pytest
(fixture tmp_path) : le fichier de scores réel n'est jamais touché.
"""

import GestionScore


def _joueur(nom, score):
    joueur = GestionScore.Joueur()
    joueur.nom = nom
    joueur.score = score
    return joueur


class TestCheckFileExistance:
    def test_fichier_absent(self, tmp_path):
        assert GestionScore.checkFileExistance(str(tmp_path / "inexistant.bin")) is False

    def test_fichier_present(self, tmp_path):
        chemin = tmp_path / "present.bin"
        chemin.write_text("")
        assert GestionScore.checkFileExistance(str(chemin)) is True


class TestSauvegardeEtChargement:
    def test_aller_retour_conserve_les_donnees(self, tmp_path):
        chemin = str(tmp_path / "scores.bin")
        GestionScore.save_scores(chemin, [_joueur("Alice", 12), _joueur("Bob", 7)])

        recharges = GestionScore.load_scores(chemin)

        assert [(j.nom, j.score) for j in recharges] == [("Alice", 12), ("Bob", 7)]

    def test_liste_vide(self, tmp_path):
        chemin = str(tmp_path / "vide.bin")
        GestionScore.save_scores(chemin, [])
        assert GestionScore.load_scores(chemin) == []

    def test_fichier_absent_renvoie_liste_vide(self, tmp_path):
        assert GestionScore.load_scores(str(tmp_path / "jamais_ecrit.bin")) == []

    def test_fichier_vide_renvoie_liste_vide(self, tmp_path):
        chemin = tmp_path / "tronque.bin"
        chemin.write_bytes(b"")
        assert GestionScore.load_scores(str(chemin)) == []
