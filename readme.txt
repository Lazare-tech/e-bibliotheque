==============================
README - e-bibliotheque Django
==============================

1️⃣ Prérequis
-------------
- Python 3.8 ou supérieur
- Pip
- Virtualenv (recommandé)

2️⃣ Installation en local
------------------------
1. Cloner le projet :
   git clone https://github.com/Lazare-tech/e-bibliotheque.git
   cd monsite
2.ou telecharger le fichier zip sur google drive
   decompresser le fichier
   cd nom_dossier
   
2. Créer et activer le virtualenv :
   python -m venv venv
   # Windows : venv\Scripts\activate
   # macOS/Linux : source venv/bin/activate

3. Installer les dépendances :
   pip install -r requirements.txt

3️⃣ Base de données
------------------
- Appliquer les migrations :
   python manage.py migrate

- Créer un superuser (optionnel) :
   python manage.py createsuperuser

4️⃣ Lancer le serveur local
---------------------------
- Démarrer le serveur Django :
   python manage.py runserver

- Visiter l'application :
   http://127.0.0.1:8000/

==============================
Fin du README
==============================

