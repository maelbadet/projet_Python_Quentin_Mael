import os
import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db  # Import correct de la dépendance de session
from db.models import League  # Import du modèle SQLAlchemy

# Création d'un router spécifique pour les routes 'leagues'
router = APIRouter()

BASE_URL = "https://api.sportmonks.com/v3/football"
API_KEY = os.getenv("APIKEY")


@router.get("/leagues/")
def get_football_leagues(db: Session = Depends(get_db)):
	"""
    Récupère les leagues de football à partir de l'API SportMonks et les insère dans la base.
    """
	if not API_KEY:
		return {"error": "La clé API n'est pas configurée"}

	endpoint = f"{BASE_URL}/leagues"
	params = {
		"include": "",
		"api_token": API_KEY
	}

	try:
		# Appel à l'API
		response = requests.get(endpoint, params=params)
		response.raise_for_status()
		data = response.json()

		leagues = data.get("data", [])
		if not leagues:
			return {"message": "Aucune ligue trouvée."}

		# Filtrer et insérer la ligue avec ID = 501
		for league in leagues:
			if league.get("id") == 501:
				# Préparer l'objet League
				new_league = League(
					name=league.get("name"),
					api_id=league.get("id"),
					country_id=league.get("country_id"),
					image_path=league.get("image_path")
				)

				# Vérifier si la ligue existe déjà
				existing_league = db.query(League).filter_by(api_id=new_league.api_id).first()
				if not existing_league:
					db.add(new_league)  # Insertion de la nouvelle ligue
				else:
					# Mise à jour des champs existants
					existing_league.name = new_league.name
					existing_league.image_path = new_league.image_path

		db.commit()  # Sauvegarde des changements

		return {"message": "La ligue Premiership a été ajoutée ou mise à jour."}

	except requests.exceptions.RequestException as e:
		return {"error": f"Erreur lors de la récupération des ligues : {str(e)}"}
