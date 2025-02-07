import os
import requests  # Utilisé pour les appels API externes
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Team import Team
from db.db import get_db

player_router = APIRouter()
BASE_URL = "https://api.sportmonks.com/v3/football"
API_KEY = os.getenv("APIKEY")


@player_router.get("/getPlayer/{team_id}", response_model=list)
def get_player_by_team(team_id: int, db: Session = Depends(get_db)):
	"""
    Récupère tous les joueurs d'une équipe donnée.
    """

	# Récupérer l'équipe depuis la base de données
	team = db.query(Team).filter_by(API_id=team_id).first()

	if not team:
		raise HTTPException(status_code=404, detail="Team not found in the database")

	# Appeler l'API externe SportMonks
	url = f"{BASE_URL}/players"
	params = {
		"api_token": API_KEY,
		"include": "teams"
	}

	try:
		response = requests.get(url, params=params)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		raise HTTPException(status_code=500, detail=f"Error contacting external API: {str(e)}")

	# Obtenir les données des joueurs
	data = response.json().get("data", [])
	if not data:
		raise HTTPException(status_code=404, detail="No players found in the external API")

	# Filtrer les joueurs par team_id
	players = []
	for player in data:
		if player.get("teams"):  # Vérifier s'il y a des équipes associées
			# Filtrer les joueurs associés à l'équipe donnée
			player_teams = [player_team for player_team in player["teams"] if player_team["team_id"] == team_id]
			if player_teams:  # Si au moins une correspondance existe
				players.append({
					"id": player["id"],
					"name": player["name"],
					"position": player.get("position_id"),
					"image_path": player["image_path"],
					"height": player.get("height"),
					"weight": player.get("weight"),
					"date_of_birth": player.get("date_of_birth"),
					"teams": player_teams  # Inclure uniquement les équipes pertinentes
				})
		else:
			continue


	# Si aucun joueur n'est trouvé pour l'équipe
	if not players:
		raise HTTPException(status_code=404, detail="No players found for the given team in the external API.")

	return players
