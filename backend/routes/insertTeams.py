import os
from datetime import datetime

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db  # Import correct de la dépendance de session
from db.models import Team  # Import du modèle SQLAlchemy

router = APIRouter()

BASE_URL = "https://api.sportmonks.com/v3/football"
API_KEY = os.getenv("APIKEY")


@router.get("/teams/")
def get_football_teams(db: Session = Depends(get_db)):
	"""
	    Récupère les equipes de football à partir de l'API SportMonks et les insère dans la base,
	    en utilisant l'id du pays pour la recherche plus precise
	    """
	if not API_KEY:
		return {"error": "La clé API n'est pas configurée"}

	endpoint = f"{BASE_URL}/teams/countries/1161"
	params = {
		"include": "",
		"api_token": API_KEY
	}

	try:
		# Appel à l'API
		response = requests.get(endpoint, params=params)
		response.raise_for_status()
		data = response.json()

		teams = data.get("data", [])
		if not teams:
			return {"message": "Aucune equipe trouvée."}

		for team in teams:
			# Préparer l'objet League
			new_team = Team(
				name=team.get("name"),
				founded=team.get("founded"),
				img_path=team.get("image_path"),
				API_id=team.get("id"),
				league_id=501,
				country_id=team.get("country_id")
			)

			# Vérifier si la ligue existe déjà
			existing_league = db.query(Team).filter_by(API_id=new_team.API_id).first()
			if not existing_league:
				db.add(new_team)  # Insertion de la nouvelle ligue
			else:
				# Mise à jour des champs existants
				existing_league.name = new_team.name
				existing_league.founded = new_team.founded
				existing_league.img_path = new_team.img_path
				existing_league.API_id = new_team.API_id
				existing_league.country_id = new_team.country_id
				existing_league.updated_at = datetime.now()

		db.commit()  # Sauvegarde des changements

		return {"message": "Les equipes on bien été ajoutée ou mise à jour."}

	except requests.exceptions.RequestException as e:
		return {"error": f"Erreur lors de la récupération des ligues : {str(e)}"}
