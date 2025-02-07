from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.tables import Season

# Connexion à la base de données (remplacez les valeurs adaptées à votre configuration)
DATABASE_URL = "sqlite:///example.db"  # Exemple avec SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Ajouter une saison
def add_season(api_id_season, date_season=None, name=None):
	new_season = Season(
		API_id_season=api_id_season,
		date_season=date_season,
		name=name
	)
	session.add(new_season)
	session.commit()
	print(f"Saison ajoutée : {new_season.name} ({new_season.API_id_season})")


# Récupérer toutes les saisons
def get_all_seasons():
	seasons = session.query(Season).all()
	for season in seasons:
		print(f"ID: {season.id}, Nom: {season.name}, Date: {season.date_season}")


# Rechercher une saison par ID
def get_season_by_id(season_id):
	season = session.query(Season).filter_by(id=season_id).first()
	if season:
		print(f"Saison trouvée : {season.name}")
	else:
		print("Saison introuvable")


# Mettre à jour une saison
def update_season_name(season_id, new_name):
	season = session.query(Season).filter_by(id=season_id).first()
	if season:
		season.name = new_name
		session.commit()
		print(f"Saison mise à jour : {season.name}")
	else:
		print("Saison introuvable")


# Supprimer une saison
def delete_season(season_id):
	season = session.query(Season).filter_by(id=season_id).first()
	if season:
		session.delete(season)
		session.commit()
		print(f"Saison supprimée : {season.name}")
	else:
		print("Saison introuvable")
