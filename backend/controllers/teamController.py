from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Team import Team
from db.db import get_db

team_router = APIRouter()


@team_router.get("/getAll", response_model=list)
def get_all_teams(db: Session = Depends(get_db)):
	"""
	    Récupère toutes les équipes de la base
	    :param db: Session DB
	    :return: Liste de toutes les équipes
	    """
	teams = db.query(Team).all()
	return [
		{
			"id": t.id,
			"name": t.name,
			"founded": t.founded,
			"img_path": t.img_path,
			"API_id": t.API_id,
			"country_id": t.country_id,
			"league_id": t.league_id
		}
		for t in teams
	]


@team_router.get("/get/{team_id}", response_model=dict)
def get_league_by_id(team_id: int, db: Session = Depends(get_db)):
	"""
	    Récupère toutes les équipes appartenant à une equipe donnée
	    :param league_id: ID de l'equipe
	    :param db: Session DB
	    :return: Liste de l'equipe
	    """
	team = db.query(Team).filter_by(API_id=team_id).first()
	if not team:
		raise HTTPException(status_code=404, detail="League not found")
	return {
		"id": team.id,
		"name": team.name,
		"founded": team.founded,
		"img_path": team.img_path,
		"API_id": team.API_id,
		"country_id": team.country_id,
		"league_id": team.league_id
	}

@team_router.get("/getAllByLeague/{league_id}", response_model=list)
def get_teams_by_league(league_id: int, db: Session = Depends(get_db)):
	"""
    Récupère toutes les équipes appartenant à une ligue donnée
    :param league_id: ID de la ligue
    :param db: Session DB
    :return: Liste des équipes
    """
	teams = db.query(Team).filter(Team.league_id == league_id).all()

	# Vérifier si aucune équipe n'existe pour l'ID de la ligue donnée
	if not teams:
		raise HTTPException(status_code=404, detail="No teams found for the given league")

	# Retourner les résultats sous forme de liste de dictionnaires
	return [
		{
			"id": t.id,
			"name": t.name,
			"founded": t.founded,
			"img_path": t.img_path,
			"API_id": t.API_id,
			"country_id": t.country_id,
			"league_id": t.league_id
		}
		for t in teams
	]
