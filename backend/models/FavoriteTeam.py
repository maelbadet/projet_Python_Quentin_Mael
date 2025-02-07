from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from db.tables import FavoriteTeam

DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)

# Création de la session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()


# Ajouter une équipe favorite
def add_favorite_team(user_id, team_id):
	favorite_team = FavoriteTeam(
		user_id=user_id,
		team_id=team_id,
		created_at=datetime.date.today(),
		updated_at=datetime.date.today()
	)
	session.add(favorite_team)
	session.commit()
	print(f"Équipe favorite ajoutée pour l'utilisateur {user_id} et l'équipe {team_id}")


# Récupérer toutes les équipes favorites
def get_all_favorite_teams():
	favorite_teams = session.query(FavoriteTeam).all()
	for favorite in favorite_teams:
		print(f"ID: {favorite.id}, Utilisateur ID: {favorite.user_id}, Équipe ID: {favorite.team_id}")


# Rechercher une équipe favorite par ID
def get_favorite_team_by_id(favorite_id):
	favorite_team = session.query(FavoriteTeam).filter_by(id=favorite_id).first()
	if favorite_team:
		print(
			f"Équipe favorite trouvée : ID: {favorite_team.id}, Utilisateur: {favorite_team.user_id}, "
			f"Équipe: {favorite_team.team_id}"
		)
	else:
		print("Équipe favorite introuvable")


# Mettre à jour une équipe favorite
def update_favorite_team(favorite_id, user_id=None, team_id=None):
	favorite_team = session.query(FavoriteTeam).filter_by(id=favorite_id).first()
	if favorite_team:
		if user_id:
			favorite_team.user_id = user_id
		if team_id:
			favorite_team.team_id = team_id
		favorite_team.updated_at = datetime.utcnow()
		session.commit()
		print(f"Équipe favorite mise à jour : ID {favorite_team.id}")
	else:
		print("Équipe favorite introuvable")


# Supprimer une équipe favorite (soft delete)
def delete_favorite_team(favorite_id):
	favorite_team = session.query(FavoriteTeam).filter_by(id=favorite_id).first()
	if favorite_team:
		favorite_team.deleted_at = datetime.utcnow()
		session.commit()
		print(f"Équipe favorite supprimée (soft delete) : ID {favorite_team.id}")
	else:
		print("Équipe favorite introuvable")


# Suppression réelle d'une équipe favorite
def delete_favorite_team_permanently(favorite_id):
	favorite_team = session.query(FavoriteTeam).filter_by(id=favorite_id).first()
	if favorite_team:
		session.delete(favorite_team)
		session.commit()
		print(f"Équipe favorite supprimée définitivement : ID {favorite_team.id}")
	else:
		print("Équipe favorite introuvable")
