from fastapi import APIRouter

# Création d'un router spécifique pour les routes 'home'
router = APIRouter()


@router.get("/")
def read_root():
	return {"message": "Bienvenue sur votre API FastAPI ! \n pour Afficher le swagger, merci d'acceder a la route http://localhost:8000/docs"}
