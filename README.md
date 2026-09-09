# Jeux console en Python — Allumettes, Devinette, Morpion

[![CI](https://github.com/Ferdisk/python-jeux-console/actions/workflows/ci.yml/badge.svg)](https://github.com/Ferdisk/python-jeux-console/actions/workflows/ci.yml)

Trois jeux en ligne de commande, jouables à deux ou contre la machine, avec
**trois stratégies d'intelligence artificielle par jeu** (aléatoire, hybride,
optimale) et un système de scores persistant.

```bash
python3 Principal.py
```

## Les stratégies implémentées

| Jeu | Facile | Moyen | Difficile |
|---|---|---|---|
| **Allumettes** | Retrait aléatoire de 1 à 3 | Hybride : optimal dans 80 % des coups, aléatoire sinon | **Stratégie de Nim** — laisse toujours un multiple de 4 à l'adversaire |
| **Devinette** | Proposition aléatoire dans l'intervalle | **Recherche binaire** — divise l'intervalle par deux à chaque coup | Hybride : recherche binaire dans 80 % des coups |
| **Morpion** | Case vide au hasard | Gagne si possible, sinon bloque l'adversaire, sinon joue au hasard | **Minimax** — explore l'arbre des coups possibles |

### Complexités

| Algorithme | Complexité | Conséquence |
|---|---|---|
| Stratégie de Nim (Allumettes) | **O(1)** | Un simple modulo : gain garanti, coût nul |
| Recherche binaire (Devinette) | **O(log n)** | ~7 coups pour trouver un nombre entre 1 et 100 |
| Minimax (Morpion) | **O(b^d)** | Exploration exhaustive : imbattable, mais le coût explose avec la taille de la grille |

## Résultats mesurés

Taux de victoire de la machine, relevés sur des parties répétées :

| Jeu | Facile | Moyen | Difficile |
|---|---|---|---|
| Allumettes | 30 % | 70 % | **100 %** |
| Devinette | 20 % | 80 % | 90 % |
| Morpion | 40 % | 60 % | **100 %** |

Les stratégies optimales (Nim, Minimax) gagnent systématiquement dès lors
qu'une victoire est atteignable — c'est la propriété attendue de ces
algorithmes, et la mesure la confirme. Les stratégies hybrides sacrifient
volontairement une part de performance pour rester imprévisibles, ce qui rend
la partie plus intéressante à jouer.

> **Sur les temps mesurés.** Le projet relève aussi une « durée moyenne de
> partie » (de 2,5 s à 20 s selon le mode). Cette mesure inclut le temps de
> réflexion du joueur humain : elle décrit l'expérience de jeu, **pas** la
> vitesse des algorithmes. Un banc de mesure limité aux parties machine contre
> machine serait nécessaire pour comparer réellement leur coût d'exécution.

## Les deux étapes du projet

Ce dépôt conserve les deux versions successives du projet :

| Version | Contenu |
|---|---|
| [`v1.01`](../../releases/tag/v1.01) | Les trois jeux, humain contre humain |
| [`v1.02`](../../releases/tag/v1.02) | Ajout des adversaires machine et des trois niveaux de difficulté |

👉 **[Voir tout ce qui a changé entre les deux](../../compare/v1.01...v1.02)** —
4 fichiers sur 7 réécrits, `Allu.py` passant de 152 à 478 lignes et `morpion.py`
de 224 à 477.

## Organisation du code

| Fichier | Rôle |
|---|---|
| `Principal.py` | Point d'entrée : lance le menu |
| `Menu.py` | Affichage du menu et aiguillage vers les jeux |
| `Allu.py` | Jeu des allumettes et ses trois stratégies |
| `devinette.py` | Jeu de la devinette et ses trois stratégies |
| `morpion.py` | Morpion, Minimax et les stratégies de blocage |
| `GestionScore.py` | Chargement et sauvegarde des scores |
| `Existe.py` | Recherche d'un joueur dans les scores enregistrés |

## Chaîne d'intégration continue

Chaque `push` déclenche quatre jobs, dont trois s'exécutent dans un conteneur
Docker `python:3.11-slim` :

| Job | Outils | Ce qu'il vérifie |
|---|---|---|
| **Tests unitaires** | pytest, pytest-cov | 40 tests sur la logique des jeux, avec mesure de couverture |
| **Analyse statique** | Ruff, Flake8, Pylint, Black | Erreurs réelles (bloquant), puis comparatif chiffré des quatre analyseurs |
| **Sécurité** | Bandit, pip-audit | Motifs dangereux dans le code, vulnérabilités connues des dépendances (bloquant) |
| **Image Docker** | Docker | L'image se construit et démarre |

À chaque tag `v*`, une [Release](../../releases) est publiée automatiquement
avec une archive téléchargeable.

### Jouer avec Docker

```bash
docker build -t jeux-console .
docker run --rm -it jeux-console
```

### Lancer les vérifications en local

```bash
pip install -r requirements-dev.txt
pytest --cov=.
bash .github/scripts/comparatif-analyseurs.sh
```

---

Projet réalisé en première année de BUT Informatique (SAÉ 1.01 puis 1.02),
repris en troisième année pour y construire une chaîne d'intégration continue.
