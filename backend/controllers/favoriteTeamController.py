from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models.FavoriteTeam import FavoriteTeam
from db.db import get_db
from datetime import timezone

favorite_router = APIRouter()


class FavoriteTeamCreate(BaseModel):
	user_id: int
	team_id: int


@favorite_router.get("/favorites/getAllByUser", response_model=list)
def get_all_favorite_teams(user_id: int, db: Session = Depends(get_db)):
	# Récupérer les équipes favorites pour un utilisateur donné
	favorite_teams = db.query(FavoriteTeam).filter_by(user_id=user_id, deleted_at=None).all()

	if not favorite_teams:
		raise HTTPException(status_code=404, detail="No favorite teams found for this user.")

	return [
		{
			"id": fv.team.id,
			"name": fv.team.name,
			"img_path": fv.team.img_path
		}
		for fv in favorite_teams
	]


@favorite_router.post("/favorite", status_code=201)
def add_favorite_team(favorite_data: FavoriteTeamCreate, db: Session = Depends(get_db)):
	# Vérifiez si l'utilisateur ou l'équipe existent déjà
	existing_favorite = db.query(FavoriteTeam).filter_by(
		user_id=favorite_data.user_id, team_id=favorite_data.team_id
	).first()

	if existing_favorite:
		raise HTTPException(status_code=400, detail="This team is already a favorite for this user.")

	# Créez un nouvel enregistrement FavoriteTeam
	favorite_team = FavoriteTeam(
		user_id=favorite_data.user_id,
		team_id=favorite_data.team_id,
		created_at=datetime.now(timezone.utc),
		updated_at=datetime.now(timezone.utc)
	)

	db.add(favorite_team)
	db.commit()
	db.refresh(favorite_team)

	return {"message": "Favorite team created successfully", "favorite_team_id": favorite_team.id}


from datetime import datetime


@favorite_router.delete("/favorite", status_code=200)
def remove_favorite_team(user_id: int, team_id: int, db: Session = Depends(get_db)):
	# Récupérer l'enregistrement correspondant
	favorite_team = db.query(FavoriteTeam).filter_by(user_id=user_id, team_id=team_id).first()

	if not favorite_team:
		raise HTTPException(status_code=404, detail="Favorite team not found.")

	# Vérifier si l'entrée est déjà supprimée
	if favorite_team.deleted_at is not None:
		raise HTTPException(status_code=400, detail="This favorite team is already removed.")

	# Mettre à jour le champ `deleted_at` avec la date/heure actuelle
	favorite_team.deleted_at = datetime.now(timezone.utc)
	db.commit()  # Enregistrer les modifications

	return {"message": "Favorite team removed successfully", "favorite_team_id": favorite_team.id}


@favorite_router.patch("/favorite", status_code=200)
def restore_favorite_team(user_id: int, team_id: int, db: Session = Depends(get_db)):
	# Récupérer l'enregistrement correspondant
	favorite_team = db.query(FavoriteTeam).filter_by(user_id=user_id, team_id=team_id).first()

	if not favorite_team:
		raise HTTPException(status_code=404, detail="Favorite team not found.")

	# Vérifier si l'entrée est déjà active
	if favorite_team.deleted_at is None:
		raise HTTPException(status_code=400, detail="This favorite team is already active.")

	# Remettre le champ `deleted_at` à `NULL`
	favorite_team.deleted_at = None
	db.commit()  # Enregistrer les modifications

	return {"message": "Favorite team restored successfully", "favorite_team_id": favorite_team.id}
