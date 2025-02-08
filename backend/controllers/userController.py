from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import bcrypt
from models.User import User
from db.db import get_db

user_router = APIRouter()


class UserCreate(BaseModel):
	name: str
	surname: str | None = None
	email: str
	telephone: str | None = None
	password: str

# Modèle des données envoyées dans la requête
class LoginRequest(BaseModel):
	email: str
	password: str


def hash_password(password: str) -> str:
	# Génère un sel (salt) et encode le mot de passe
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed_password.decode('utf-8')


@user_router.post("/users", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
	# Hachage du mot de passe
	hashed_password = hash_password(user.password)

	# Création de l'utilisateur
	new_user = User(
		name=user.name,
		surname=user.surname,
		email=user.email,
		telephone=user.telephone,
		password=hashed_password,
		created_at=datetime.now(timezone.utc),
		updated_at=datetime.now(timezone.utc),
	)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)

	return {"message": "User created successfully", "id": new_user.id}

@user_router.get("/getAll", response_model=list)
def get_all_user(db: Session = Depends(get_db)):
	user = db.query(User).all()
	return [
		{
			"name": u.name,
			"surname": u.surname,
			"email": u.email,
			"telephone": u.telephone,
			"password": u.password
		}
		for u in user
	]

@user_router.post("/login", response_model=dict)
def login(request: LoginRequest, db: Session = Depends(get_db)):
	# Recherche dans la base de données par email
	user = db.query(User).filter(User.email == request.email).first()

	# Vérification si l'utilisateur existe
	if not user:
		raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

	# Vérification du mot de passe
	if not bcrypt.checkpw(request.password.encode('utf-8'), user.password.encode('utf-8')):
		raise HTTPException(status_code=400, detail="Mot de passe incorrect")

	# Retourne les informations utilisateur
	return {
		"message": "Connexion réussie",
		"id": user.id,
		"name": user.surname,
	}
