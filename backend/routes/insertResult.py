import os
from datetime import datetime

import requests
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.db import get_db  # Import correct de la dépendance de session
from db.tables import Result  # Import du modèle SQLAlchemy

router = APIRouter()

BASE_URL = "https://api.sportmonks.com/v3/football"
API_KEY = os.getenv("APIKEY")


@router.get("/results/")
def get_football_season(db: Session = Depends(get_db)):
	"""
	    Récupère les equipes de football à partir de l'API SportMonks et les insère dans la base,
	    en utilisant l'id du pays pour la recherche plus precise
	    """
	if not API_KEY:
		return {"error": "La clé API n'est pas configurée"}

	endpoint = f"{BASE_URL}/schedules/seasons/825"
	params = {
		"include": "",
		"api_token": API_KEY
	}

	try:
		# Appel à l'API
		response = requests.get(endpoint, params=params)
		response.raise_for_status()
		data = response.json()

		results = data.get("data", [])
		if not results:
			return {"message": "Aucune equipe trouvée."}

		for result in results:
			# Vérification si c'est la ligue avec league_id = 501
			if result.get("league_id") == 501:

				# Parcourt les "rounds" dans chaque "result"
				rounds = result.get("rounds", [])
				for rnd in rounds:

					# Parcourt les "fixtures" dans chaque "round"
					fixtures = rnd.get("fixtures", [])
					for fixture in fixtures:
						# Initialisation des scores pour ce fixture
						goal_set = 0
						goal_conceded = 0

						# Parcourt les "scores" dans chaque "fixture"
						scores = fixture.get("scores", [])
						for score in scores:
							score_data = score.get("score", {})  # Extraire les données dans "score"
							participant = score_data.get("participant")
							goals = score_data.get("goals", 0)

							# Mise à jour des scores "home" et "away" avec la bonne structure
							if participant == "home" and goals > goal_set:
								goal_set = goals  # Mise à jour des buts marqués par l'équipe "home"
							if participant == "away" and goals > goal_conceded:
								goal_conceded = goals  # Mise à jour des buts concédés contre "away"

						# Créer une nouvelle instance de résultat
						new_result = Result(
							name=fixture.get("name"),
							season_id=result.get("season_id"),
							starting_at=fixture.get("starting_at"),
							result_info=fixture.get("result_info"),
							goal_set=goal_set,
							goal_conceded=goal_conceded,
						)

						# Vérifie si le fixture existe déjà dans la base via "name", "starting_at" et éventuellement "season_id"
						existing_result = db.query(Result).filter_by(
							name=new_result.name,
							starting_at=new_result.starting_at,
							season_id=new_result.season_id
						).first()

						if not existing_result:
							# Ajouter le résultat si inexistant
							db.add(new_result)
						else:
							# Mettre à jour les champs existants
							existing_result.result_info = new_result.result_info
							existing_result.goal_set = new_result.goal_set
							existing_result.goal_conceded = new_result.goal_conceded

				# Sauvegarde des changements dans la base
				db.commit()
		return {"message": "Les resultats on bien été ajoutée ou mise à jour."}

	except requests.exceptions.RequestException as e:
		return {"error": f"Erreur lors de la récupération des ligues : {str(e)}"}
