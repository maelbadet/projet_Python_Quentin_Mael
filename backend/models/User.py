from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime


from db.tables import User

DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)

# Création de la session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()


# Ajouter un utilisateur
def add_user(name, surname=None, email=None, telephone=None, password=None):
	new_user = User(
		name=name,
		surname=surname,
		email=email,
		telephone=telephone,
		password=password,
		created_at=datetime.date.today(),
		updated_at=datetime.date.today(),
	)
	session.add(new_user)
	session.commit()
	print(f"Utilisateur ajouté : {new_user.name} {new_user.surname}")


# Récupérer tous les utilisateurs
def get_all_users():
	users = session.query(User).all()
	for user in users:
		print(f"ID: {user.id}, Nom: {user.name} {user.surname}, Email: {user.email}")


# Rechercher un utilisateur par ID
def get_user_by_id(user_id):
	user = session.query(User).filter_by(id=user_id).first()
	if user:
		print(f"Utilisateur trouvé : {user.name} {user.surname}, Email: {user.email}")
	else:
		print("Utilisateur introuvable")


# Mettre à jour les informations d'un utilisateur
def update_user_info(user_id, name=None, surname=None, email=None, telephone=None, password=None):
	user = session.query(User).filter_by(id=user_id).first()
	if user:
		if name:
			user.name = name
		if surname:
			user.surname = surname
		if email:
			user.email = email
		if telephone:
			user.telephone = telephone
		if password:
			user.password = password
		user.updated_at = datetime.utcnow()
		session.commit()
		print(f"Utilisateurs mis à jour : {user.name} {user.surname}")
	else:
		print("Utilisateur introuvable")


# Supprimer un utilisateur (soft delete en utilisant deleted_at)
def delete_user(user_id):
	user = session.query(User).filter_by(id=user_id).first()
	if user:
		user.deleted_at = datetime.utcnow()
		session.commit()
		print(f"Utilisateur supprimé (soft delete) : {user.name} {user.surname}")
	else:
		print("Utilisateur introuvable")


# Suppression réelle d'un utilisateur de la base de données
def delete_user_permanently(user_id):
	user = session.query(User).filter_by(id=user_id).first()
	if user:
		session.delete(user)
		session.commit()
		print(f"Utilisateur supprimé définitivement : {user.name} {user.surname}")
	else:
		print("Utilisateur introuvable")
