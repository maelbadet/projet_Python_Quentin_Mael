from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.Result import Result
from db.db import get_db

result_router = APIRouter()

# Récupérer tous les résultats
@result_router.get("/getAll", response_model=list)
def get_all_results(db: Session = Depends(get_db)):
	"""
	Recupere tous les resultats de toutes les saisons
	:param db: Session DB
	:return: Liste de tous les résultats
	"""
	results = db.query(Result).all()
	return [
		{
			"id": r.id,
			"name": r.name,
			"season_id": r.season_id,
			"starting_at": r.starting_at,
			"goal_conceded": r.goal_conceded,
			"goal_set": r.goal_set,
		}
		for r in results
	]


# Récupérer un résultat par ID
@result_router.get("/get/{season_id}", response_model=list)
def get_results_by_season(season_id: int, db: Session = Depends(get_db)):
	"""
    Récupère tous les résultats de la saison donnée.
    :param season_id: ID de la saison
    :param db: Session DB
    :return: Liste de résultats pour la saison donnée
    """
	results = db.query(Result).filter_by(season_id=season_id).all()

	# Vérifier si aucun résultat n'est trouvé
	if not results:
		raise HTTPException(status_code=404, detail="No results found for the given season")

	# Retourner tous les résultats sous forme de liste de dictionnaires
	return [
		{
			"id": r.id,
			"name": r.name,
			"season_id": r.season_id,
			"starting_at": r.starting_at,
			"goal_conceded": r.goal_conceded,
			"goal_set": r.goal_set,
		}
		for r in results
	]


@result_router.get("/latest-matches", response_model=list)
def get_latest_matches(db: Session = Depends(get_db)):
	"""
		Recupere les 5 derniers matchs joués depuis la base de donnee
		:param db: Session DB
		:return: Récupere les 5 derniers matchs jouée depuis la base de donnee
		"""
	# Requêter les 5 derniers matchs par date (starting_at) dans l'ordre décroissant
	results = db.query(Result).order_by(Result.starting_at.desc()).limit(5).all()

	# Si aucun match n'est trouvé
	if not results:
		raise HTTPException(status_code=404, detail="No results found")

	# Retourner les résultats comme liste de dictionnaires
	return [
		{
			"id": r.id,
			"name": r.name,
			"season_id": r.season_id,
			"starting_at": r.starting_at,
			"goal_conceded": r.goal_conceded,
			"goal_set": r.goal_set,
		}
		for r in results
	]