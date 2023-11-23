FROM python:3.8

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY requirements.txt /app/
COPY . /app/

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application va écouter
EXPOSE 7000

RUN python manage.py runserver 7000
