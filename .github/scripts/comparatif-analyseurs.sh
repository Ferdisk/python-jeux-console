#!/usr/bin/env bash
#
# Compare les analyseurs statiques Python sur ce projet : temps d'exécution
# et nombre de remarques produites, avec une configuration identique
# (longueur de ligne 120) pour que la comparaison porte sur les règles.
#
# Ce script sert à la fois dans le pipeline et en local :
#     bash .github/scripts/comparatif-analyseurs.sh
#
set -u

SOURCES=(Allu.py devinette.py morpion.py Menu.py Principal.py GestionScore.py Existe.py)

maintenant() { python -c 'import time; print(f"{time.time():.3f}")'; }
duree() { python -c "print(f'{$2 - $1:.2f}')"; }

# Exécute un outil, renvoie « durée|nombre de remarques ».
mesurer() {
    local motif="$1"; shift
    local debut fin sortie nb
    debut=$(maintenant)
    sortie=$("$@" 2>&1)
    fin=$(maintenant)
    nb=$(printf '%s\n' "$sortie" | grep -cE "$motif" || true)
    printf '%s|%s' "$(duree "$debut" "$fin")" "$nb"
}

# Préchauffage : le premier outil lancé paie le coût de démarrage de
# l'interpréteur et la construction des caches. Sans cette passe blanche,
# il apparaîtrait artificiellement plus lent que les suivants.
echo "Préchauffage des outils..." >&2
for outil in "ruff check" "flake8" "pylint --score=n" "black --check"; do
    $outil Existe.py >/dev/null 2>&1 || true
done

echo "Comparatif des analyseurs statiques" >&2

# Ruff n'active qu'un petit jeu de règles par défaut (E4, E7, E9, F).
# On le mesure deux fois : tel quel, puis avec le même périmètre que Flake8,
# faute de quoi la comparaison des nombres de remarques n'aurait aucun sens.
RUFF=$(mesurer ':[0-9]+:[0-9]+:' ruff check --output-format=concise "${SOURCES[@]}")
RUFF_ETENDU=$(mesurer ':[0-9]+:[0-9]+:' ruff check --select E,W,F --output-format=concise "${SOURCES[@]}")
FLAKE8=$(mesurer ':[0-9]+:[0-9]+:' flake8 "${SOURCES[@]}")
PYLINT=$(mesurer ':[0-9]+: \[' pylint --output-format=parseable --score=n "${SOURCES[@]}")
BLACK=$(mesurer '^would reformat' black --check "${SOURCES[@]}")

ligne() {
    local nom="$1" resultat="$2" role="$3"
    printf '| %s | %s s | %s | %s |\n' "$nom" "${resultat%%|*}" "${resultat##*|}" "$role"
}

{
    echo "## Comparatif des analyseurs statiques"
    echo
    echo "Même périmètre (7 fichiers) et même longueur de ligne (120) pour tous."
    echo "Chaque outil est préchauffé avant mesure, pour ne pas imputer au premier"
    echo "lancé le coût de démarrage de l'interpréteur."
    echo
    echo "| Outil | Durée | Remarques | Rôle |"
    echo "|---|---|---|---|"
    ligne "Ruff (défaut)" "$RUFF" "Écrit en Rust ; par défaut seules les règles E4/E7/E9/F sont actives"
    ligne "Ruff (E,W,F)" "$RUFF_ETENDU" "Même périmètre de règles que Flake8, pour une comparaison équitable"
    ligne "Flake8" "$FLAKE8" "Style (PEP 8) et erreurs simples"
    ligne "Pylint" "$PYLINT" "Analyse approfondie, conventions de nommage, conception"
    ligne "Black"  "$BLACK"  "Formateur : nombre de fichiers à reformater"
} | if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then tee -a "$GITHUB_STEP_SUMMARY"; else cat; fi
