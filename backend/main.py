from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.db import get_db

app = FastAPI()

@app.get("/")
def read_root():
	return {"message": "Bienvenue sur votre API FastAPI !"}
# Endpoint pour tester la connexion à la base de données
@app.get("/test-db/")
def test_db_connection(db: Session = Depends(get_db)):
	try:
		# Exécuter une requête simple pour vérifier la connexion
		db.execute("SELECT 1")
		return {"status": "success", "message": "Connexion à la base de données réussie"}
	except Exception as e:
		return {"status": "error", "message": f"Erreur de connexion : {str(e)}"}
