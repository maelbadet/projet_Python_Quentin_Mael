from datetime import datetime, timezone

from fastapi import APIRouter, Depends
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