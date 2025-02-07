from fastapi import FastAPI
from routes import home, insertLeagues, insertTeams, insertSeason, insertResult
from controllers.leagueController import league_router
from controllers.resultController import result_router
from controllers.seasonController import season_router
from controllers.teamController import team_router
from controllers.playerController import player_router


app = FastAPI(
	title="Football API",
	description="Une API pour la gestion des ligues, équipes, saisons et résultats",
	version="1.0",
	docs_url="/docs",  # URL pour Swagger UI
	redoc_url="/redoc"  # Redoc UI
)

# Ajout des routers avec des préfixes propres
app.include_router(home.router, prefix="", tags=["Accueil"])
app.include_router(insertLeagues.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertTeams.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertSeason.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertResult.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])

# Inclusion des routers des contrôleurs
app.include_router(league_router, prefix="/api/v1/leagues", tags=["routes pour les ligues"])
app.include_router(result_router, prefix="/api/v1/results", tags=["routes pour les resultats"])
app.include_router(season_router, prefix="/api/v1/seasons", tags=["routes pour les saisons"])
app.include_router(team_router, prefix="/api/v1/teams", tags=["routes pour les equipes"])
app.include_router(player_router, prefix="/api/v1/player", tags=["routes pour les joueurs"])
