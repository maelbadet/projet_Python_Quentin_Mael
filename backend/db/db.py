from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from .tables import Base

# Récupérer l'URL de connexion de la base de données à partir des variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/db_name")

# Création de l'engin SQLAlchemy (connexion à la base)
engine = create_engine(DATABASE_URL)

# Création de la classe Session pour gérer les sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# Dépendance pour obtenir une session de connexion à la base
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
