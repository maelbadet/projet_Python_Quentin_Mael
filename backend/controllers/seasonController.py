from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Season import Season
from db.db import get_db

season_router = APIRouter()


@season_router.get("/getAll", response_model=list)
def get_all_leagues(db: Session = Depends(get_db)):
	leagues = db.query(Season).all()
	return [
		{
			"id": l.id,
			"API_id_season": l.API_id_season,
			"date_season": l.date_season,
			"name": l.name
		}
		for l in leagues
	]


@season_router.get("/get/{season_id}", response_model=dict)
def get_league_by_id(season_id: int, db: Session = Depends(get_db)):
	season = db.query(Season).filter_by(id=season_id).first()
	if not season:
		raise HTTPException(status_code=404, detail="League not found")
	return {
		"id": season.id,
		"API_id_season": season.API_id_season,
		"date_season": season.date_season,
		"name": season.name
	}
