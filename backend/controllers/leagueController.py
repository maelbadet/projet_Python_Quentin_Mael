from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Leagues import League
from db.db import get_db

league_router = APIRouter()


@league_router.get("/getAll", response_model=list)
def get_all_leagues(db: Session = Depends(get_db)):
	leagues = db.query(League).all()
	return [
		{"id": l.id,
		 "name": l.name,
		 "country_id": l.country_id,
		 "image_path": l.image_path
		 }
		for l in leagues
	]


@league_router.get("/get/{league_id}", response_model=dict)
def get_league_by_id(league_id: int, db: Session = Depends(get_db)):
	league = db.query(League).filter_by(id=league_id).first()
	if not league:
		raise HTTPException(status_code=404, detail="League not found")
	return {
		"id": league.id,
		"name": league.name,
		"country_id": league.country_id,
		"image_path": league.image_path
	}
