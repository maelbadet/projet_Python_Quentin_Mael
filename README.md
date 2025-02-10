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
- #### Route pour recuperer les informations de l'api et les stockees en base :
  - http://localhost:8000/api/v1/insert/leagues/ : permet l'insertion dans la base de donne de la ligue premiership
  - http://localhost:8000/api/v1/insert/teams/ : permet l'insertion dans la base de donne des equipes de premiership
  - http://localhost:8000/api/v1/insert/season/ : permet l'insertion dans la base des saisons pour l'id de league 501
  - http://localhost:8000/api/v1/insert/results/ : permet l'insertion dans la base des resultats pour l'id de saison 825
- #### Route pour recuperer les informations de notre base pour le front
  - <span style="color: #e51bcc">routes pour la recuperation des leagues</span>
    - http://localhost:8000/api/v1/leagues/getAll : affiche toutes les leagues de la base de donnee
    - http://localhost:8000/api/v1/leagues/get/{league_id} : affiche la ligue avec le bon id
  - <span style="color: #e51bcc">routes pour la recuperation des resultats</span>
    - http://localhost:8000/api/v1/results/getAll : affiche tous les resultats de toutes les saisons
    - http://localhost:8000/api/v1/results/get/{season_id} : affiche les resultats de la saison donnee
    - http://localhost:8000/api/v1/results/latest-matches : pour afficher les 5 derniers matchs de notre bdd
  - <span style="color: #e51bcc">routes pour la recuperation des saisons</span>
    - http://localhost:8000/api/v1/seasons/getAll : Recupere toutes les saisons de la base de donnee
    - http://localhost:8000/api/v1/seasons/get/{season_id} : recupere la saison par son id
  - <span style="color: #e51bcc">routes pour la recuperation des equipes</span>
    - http://localhost:8000/api/v1/seasons/getAll : Recupere toutes les saisons de la base de donnee
    - http://localhost:8000/api/v1/seasons/get/{season_id} : recupere la saison par son id
  - <span style="color: #e51bcc">routes pour la recuperation de la liste des joueurs par equipe</span>
      - http://localhost:8000/api/v1/player/getPlayer/{team_id} : permet la recuperations des joueurs par un id d'equipe


## FRONTEND
### -- **Important** --
Avant de lancer l'application, il faut penser a bien installé les librairies utiliser pour ne 
pas avoir de probleme :

### Différents Parcours existant :
- **Parcours 1** : depuis la page accueil rentrer le nom d'une equipe dans la barre de rechercher
afin d'arriver sur la page de détail lié à cette équipe et ces futurs / récents match jouer
- **Parcours 2** : depuis la page accueil cliquer sur le logo / nom d'une league afin d'accéder aux
différentes informations des prochains match / ancien match de cette ligue ainsi que le classement
de toutes les équipes présente dans la league
- **Parcours 3** : depuis la page accueil ou depuis une page de league appuyer sur l'un des match
afin d'avoir des informations supplémentaires concernant le match
