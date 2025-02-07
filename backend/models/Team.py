from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.tables import Team

# Connexion à la base de données (remplacez les valeurs adaptées à votre configuration)
DATABASE_URL = "sqlite:///example.db"  # Exemple avec SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()


import datetime


# Ajouter une équipe
def add_team(name, founded=None, img_path=None, api_id=None, country_id=None, league_id=None):
	new_team = Team(
		name=name,
		founded=founded,
		img_path=img_path,
		API_id=api_id,
		country_id=country_id,
		league_id=league_id,
		created_at=datetime.date.today(),
		updated_at=datetime.date.today()
	)
	session.add(new_team)
	session.commit()
	print(f"Équipe ajoutée : {new_team.name}")


# Récupérer toutes les équipes
def get_all_teams():
	teams = session.query(Team).all()
	for team in teams:
		print(f"ID: {team.id}, Nom: {team.name}, Fondé: {team.founded}")


# Rechercher une équipe par ID
def get_team_by_id(team_id):
	team = session.query(Team).filter_by(id=team_id).first()
	if team:
		print(f"Équipe trouvée : {team.name}")
	else:
		print("Équipe introuvable")


# Mettre à jour le nom d'une équipe
def update_team_name(team_id, new_name):
	team = session.query(Team).filter_by(id=team_id).first()
	if team:
		team.name = new_name
		team.updated_at = datetime.date.today()
		session.commit()
		print(f"Équipe mise à jour : {team.name}")
	else:
		print("Équipe introuvable")


# Supprimer une équipe
def delete_team(team_id):
	team = session.query(Team).filter_by(id=team_id).first()
	if team:
		session.delete(team)
		session.commit()
		print(f"Équipe supprimée : {team.name}")
	else:
		print("Équipe introuvable")
