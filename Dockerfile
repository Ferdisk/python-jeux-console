# Image permettant de jouer sans installer Python.
#
# Construire :  docker build -t jeux-console .
# Jouer      :  docker run --rm -it jeux-console
#
# Le -it est indispensable : les trois jeux lisent les coups au clavier.

FROM python:3.11-slim

WORKDIR /app

# Le projet n'utilise que la bibliothèque standard : aucune dépendance
# à installer, ce qui garde l'image minimale.
COPY Principal.py Menu.py Allu.py devinette.py morpion.py GestionScore.py Existe.py ./

# Les scores sont écrits dans le répertoire de travail ; ce volume permet
# de les conserver d'une partie à l'autre.
VOLUME ["/app/data"]

CMD ["python", "Principal.py"]
