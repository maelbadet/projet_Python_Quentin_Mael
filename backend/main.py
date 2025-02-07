from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import home, insertLeagues, insertTeams, insertSeason, insertResult
from controllers.leagueController import league_router
from controllers.resultController import result_router
from controllers.seasonController import season_router

app = FastAPI(
	title="Football API",
	description="Une API pour la gestion des ligues, équipes, saisons et résultats",
	version="1.0",
	docs_url="/docs",  # URL pour Swagger UI
	redoc_url="/redoc"  # Redoc UI
)

# Définition des origines autorisées
origins = [
    "http://localhost:3000",  # Autorise ton frontend local
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Autorise uniquement ces origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les headers
)

# Ajout des routers avec des préfixes propres
app.include_router(home.router, prefix="", tags=["Accueil"])
app.include_router(insertLeagues.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertTeams.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertSeason.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertResult.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])

# Inclusion des routers des contrôleurs
app.include_router(league_router, prefix="/api/v1/leagues", tags=["Controllers"])
app.include_router(result_router, prefix="/api/v1/results", tags=["Controllers"])
app.include_router(season_router, prefix="/api/v1/seasons", tags=["Controllers"])
