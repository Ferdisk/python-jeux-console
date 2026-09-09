"""Fixtures partagées par les tests.

Les classes Joueur / Jeux / Score du projet ne définissent que des annotations
(pas de __init__), on fournit donc des fabriques pour construire des instances
utilisables dans les tests.
"""

import pytest

import Existe


def _joueur(nom, score):
    joueur = Existe.Joueur()
    joueur.nom = nom
    joueur.score = score
    return joueur


def _jeu(joueurs):
    jeu = Existe.Jeux()
    jeu.tab_score = list(joueurs)
    jeu.nb_joueur = len(joueurs)
    return jeu


@pytest.fixture
def fabrique_joueur():
    return _joueur


@pytest.fixture
def score_vide():
    """Un objet Score dont les trois jeux existent mais sans aucun joueur."""
    score = Existe.Score()
    score.Devinette = _jeu([])
    score.Morpion = _jeu([])
    score.Allumettes = _jeu([])
    return score


@pytest.fixture
def score_avec_joueurs():
    """Un objet Score contenant Alice et Bob au Morpion."""
    score = Existe.Score()
    score.Devinette = _jeu([])
    score.Morpion = _jeu([_joueur("Alice", 3), _joueur("Bob", 1)])
    score.Allumettes = _jeu([])
    return score


@pytest.fixture
def grille_vide():
    return [[" "] * 3 for _ in range(3)]
