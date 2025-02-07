from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.tables import League

# Connexion à la base de données (remplacez les valeurs adaptées à votre configuration)
DATABASE_URL = "sqlite:///example.db"  # Exemple avec SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()


# Exemple : Ajouter un nouvel enregistrement
def add_league(name, api_id, country_id, image_path=None):
	league = League(name=name, api_id=api_id, country_id=country_id, image_path=image_path)
	session.add(league)
	session.commit()  # Valider les modifications
	print(f"Ligue ajoutée avec succès : {league.name}")


# Exemple : Récupérer toutes les ligues
def get_all_leagues():
	leagues = session.query(League).all()
	for league in leagues:
		print(f"ID: {league.id}, Name: {league.name}, Country ID: {league.country_id}")


# Exemple : Trouver une ligue par son `id`
def get_league_by_id(league_id):
	league = session.query(League).filter_by(id=league_id).first()
	if league:
		print(f"Ligue trouvée : {league.name}")
	else:
		print("Ligue introuvable.")


# Exemple : Mettre à jour une entrée existante
def update_league_name(league_id, new_name):
	league = session.query(League).filter_by(id=league_id).first()
	if league:
		league.name = new_name
		session.commit()
		print(f"Ligue mise à jour : {league.name}")
	else:
		print("Ligue introuvable.")


# Exemple : Supprimer une ligue
def delete_league(league_id):
	league = session.query(League).filter_by(id=league_id).first()
	if league:
		session.delete(league)
		session.commit()
		print(f"Ligue supprimée : {league.name}")
	else:
		print("Ligue introuvable.")
