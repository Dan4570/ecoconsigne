# Dockerfile
FROM python:3.11-slim

# Créer le dossier de travail
WORKDIR /app

# Copier le code dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ouvrir le port 8000
EXPOSE 8000

# Commande pour lancer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
