# Projet Python sur les equipes de football

## Introduction
Le but est de faire une application web permettant à un utilisateur de rechercher son equipe et 
d'avoir affiché les informations comme ses derniers matchs, les rencontres a venir le club, etc.

## Technologies utilisee 
- **Docker** : Utilisation de Docker pour creer le conteneur de la base de donnee
- **Python** : Pour la partie *backend* et *frontend* de l'application
- **https://docs.sportmonks.com/football** : Utilisation de l'api sportmonks pour obtenir les informations 
sur les clubs de foot

## Gestion de projet
- **trello** : https://trello.com/b/Sfd6ubWS/projetpythonquentinmael
- **git** : https://github.com/maelbadet/projet_Python_Quentin_Mael
- **figma** : https://www.figma.com/design/N5RxDKr8nCaA5dvRpMtxFd/projet-3-quentin-et-mael?node-id=0-1&m=dev&t=2qKgEEN44dGKTI6r-1

## Routes API importantes
### **À cause de l'abonnement limite gratuit, on n'a acces qu'à des donnes limitees (dates, leagues, pays, etc.)**
L'API possedents plusieurs routes qui vont nous etres utiles : 
- https://api.sportmonks.com/v3 est l'URL de base par laquelle toutes les requetes vont etre, faites
- https://api.sportmonks.com/v3/core/ est la base que l'on va utiliser pour les filtres globaux, comme le pays, le continent, etc.
- https://api.sportmonks.com/v3/football/ est l'url pour rechercher tout ce qui va concerner le foot (equipe, matchs, joueurs, etc.)
- https://api.sportmonks.com/v3/core/continents Recuperer tous les continents
- https://api.sportmonks.com/v3/core/continents/1?include=countries; Recuperer les pays du continent 1
- Recuperation de l'information d'un pays par 2 manieres possible : 
  - https://api.sportmonks.com/v3/core/countries/17?api_token={{api_token}}&include=leagues; afficher les informations de la france par son id
  - https://api.sportmonks.com/v3/core/countries/search/france?api_token={{api_token}}&include=leagues; par son nom
- https://api.sportmonks.com/v3/core/types?api_token={{api_token}}&include= Recupere les types d'information d'un match (mi-temps, var, but, etc.) 
- Recuperations de l'information des leagues
  - https://api.sportmonks.com/v3/football/leagues?api_token={{api_token}}&include= : acceder a toutes les leagues
  - https://api.sportmonks.com/v3/football/leagues/271?api_token={{api_token}}&include= : acceder a une league via son id
- https://api.sportmonks.com/v3/football/seasons?api_token={{api_token}}&include= Recuperation des saisons
- https://api.sportmonks.com/v3/football/teams?api_token={{api_token}}&include= Recuperer toutes les equipes
- https://api.sportmonks.com/v3/football/players?api_token={{api_token}}&include= Recupere tous les joueurs
- https://api.sportmonks.com/v3/football/players/search/JamesForrest?api_token={{api_token}}&include= recupere un joueur par nom
- https://api.sportmonks.com/v3/football/squads/teams/53?api_token={{api_token}}&include= recuperer les joueurs de l'equipe (53 ici)
- https://api.sportmonks.com/v3/football/schedules/seasons/1927/teams/53?api_token={{api_token}}&include= recuperer les informations d'une saison

## Lancement du projet
Pour lancer le projet, installer toutes les dependances et lancer les differents server, il suffit de lancer la commande docker
`docker-compose up --build`. 
Une fois le build fait une fois, il suffira de lancer la commande `docker-compose up` pour lancer le projet et les servers
## BACKEND

### Sources : 
  - fastapi : https://fastapi.tiangolo.com/fr/tutorial/#installer-fastapi
  - uvicorn : https://fastapi.tiangolo.com/fr/tutorial/#installer-fastapi
  - pytest : https://docs.pytest.org/en/stable/getting-started.html
  - dotenv : https://pypi.org/project/python-dotenv/

### Les routes
Les differentes routes utilisees dans le projet sont listé dans le swagger, mais je préfère les 
remettre ici pour la simpliciter de lectures. Voici la liste des routes ainsi que les methodes d'acces : 
- http://localhost:8000/ : affiche la page d'accueil de mon backend
- http://localhost:8000/docs : affiche le swagger avec les differentes routes disponnibles
- http://localhost:8000/api/v1/insert/leagues/ : permet l'insertion dans la base de donne de la ligue premiership
- http://localhost:8000/api/v1/insert/teams/ : permet l'insertion dans la base de donne des equipes de premiership
- http://localhost:8000/api/v1/insert/season/ : permet l'insertion dans la base des saisons pour l'id de league 501

## FRONTEND
### -- **Important** --
Avant de lancer l'application, il faut penser a bien installé les librairies utiliser pour ne 
pas avoir de probleme :
Liste des librairies : 
- blablabla
- blablabla
- blablabla
- blablabla

### Les routes
Les differentes routes utilisees sont les suivantes : 
- route 1 : expliquer à quoi servent les routes
- route 2 : expliquer à quoi servent les routes
- route 3 : expliquer à quoi servent les routes
- route 4 : expliquer à quoi servent les routes
- route 5 : expliquer à quoi servent les routes

Mettre des explications sur le fonctionnement de l'application coté front