import os
from datetime import datetime

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db  # Import correct de la dépendance de session
from db.tables import Season  # Import du modèle SQLAlchemy

router = APIRouter()

BASE_URL = "https://api.sportmonks.com/v3/football"
API_KEY = os.getenv("APIKEY")


@router.get("/season/")
def get_football_season(db: Session = Depends(get_db)):
	"""
	    Récupère les equipes de football à partir de l'API SportMonks et les insère dans la base,
	    en utilisant l'id du pays pour la recherche plus precise
	    """
	if not API_KEY:
		return {"error": "La clé API n'est pas configurée"}

	endpoint = f"{BASE_URL}/seasons"
	params = {
		"include": "",
		"api_token": API_KEY
	}

	try:
		# Appel à l'API
		response = requests.get(endpoint, params=params)
		response.raise_for_status()
		data = response.json()

		seasons = data.get("data", [])
		if not seasons:
			return {"message": "Aucune equipe trouvée."}

		for season in seasons:
			if season.get("league_id") == 501:
				new_season = Season(
					API_id_season=season.get("id"),
					date_season=season.get("starting_at"),
					name=season.get("name")
				)
				# Vérifier si la ligue existe déjà
				existing_league = db.query(Season).filter_by(API_id_season=new_season.API_id_season).first()
				if not existing_league:
					db.add(new_season)  # Insertion de la nouvelle ligue
				else:
					# Mise à jour des champs existants
					existing_league.API_id_season = new_season.API_id_season
					existing_league.name = new_season.name
					existing_league.date_season = new_season.date_season

			db.commit()  # Sauvegarde des changements

		return {"message": "Les saisons on bien été ajoutée ou mise à jour."}

	except requests.exceptions.RequestException as e:
		return {"error": f"Erreur lors de la récupération des ligues : {str(e)}"}
