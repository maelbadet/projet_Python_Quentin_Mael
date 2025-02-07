# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Installer les dépendances système nécessaires (optionnel)
RUN apt-get update && apt-get install -y curl && apt-get clean

# Télécharger wait-for-it.sh
RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

# Copier les fichiers d'application dans le conteneur
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir fastapi uvicorn pytest python-dotenv sqlalchemy pymysql cryptography requests==2.31.0

# Définir le script d'entrée
ENTRYPOINT ["./wait-for-it.sh", "db:3306", "--"]

# Lancer Uvicorn après que la base de données soit prête
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Expose le port 8000
EXPOSE 8000