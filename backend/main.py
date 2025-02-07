from fastapi import FastAPI
from routes import home, insertLeagues, insertTeams, insertSeason, insertResult

app = FastAPI()

# Ajout des routers avec des préfixes propres
app.include_router(home.router, prefix="", tags=["Accueil"])
app.include_router(insertLeagues.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertTeams.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertSeason.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
app.include_router(insertResult.router, prefix="/api/v1/insert", tags=["Recuperation et insertion dans la base de donnee"])
