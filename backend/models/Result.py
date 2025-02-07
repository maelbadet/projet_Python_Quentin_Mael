from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.tables import Result

# Connexion à la base de données (remplacez les valeurs adaptées à votre configuration)
DATABASE_URL = "sqlite:///example.db"  # Exemple avec SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Ajouter un nouveau résultat
def add_result(season_id, name, starting_at, result_info=None, goal_conceded=None, goal_set=None):
	new_result = Result(
		season_id=season_id,
		name=name,
		starting_at=starting_at,
		result_info=result_info,
		goal_conceded=goal_conceded,
		goal_set=goal_set
	)
	session.add(new_result)
	session.commit()
	print(f"Résultat ajouté : {new_result.name}")


# Récupérer tous les résultats
def get_all_results():
	results = session.query(Result).all()
	for result in results:
		print(f"ID: {result.id}, Nom: {result.name}, Date: {result.starting_at}")


# Rechercher un résultat par ID
def get_result_by_id(result_id):
	result = session.query(Result).filter_by(id=result_id).first()
	if result:
		print(f"Résultat trouvé : {result.name}")
	else:
		print("Résultat introuvable")


# Mettre à jour un résultat
def update_result(result_id, new_name):
	result = session.query(Result).filter_by(id=result_id).first()
	if result:
		result.name = new_name
		session.commit()
		print(f"Résultat mis à jour : {result.name}")
	else:
		print("Résultat introuvable")


# Supprimer un résultat
def delete_result(result_id):
	result = session.query(Result).filter_by(id=result_id).first()
	if result:
		session.delete(result)
		session.commit()
		print(f"Résultat supprimé : {result.name}")
	else:
		print("Résultat introuvable")
