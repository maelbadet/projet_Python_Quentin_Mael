document.addEventListener("DOMContentLoaded", async () => {
    const allTeamsContainer = document.getElementById("toutes-les-equipes");
    const teamsContainer = document.getElementById("teams-container"); // Conteneur pour les cartes

    try {
        const userId = localStorage.getItem("userId"); // Récupération de l'utilisateur connecté
        if (!userId) {
            alert("Vous devez être connecté pour voir vos favoris.");
            return;
        }

        // Appel pour récupérer les équipes favorites de l'utilisateur
        const favoritesResponse = await fetch(`http://localhost:8000/api/v1/users/favorites/getAllByUser?user_id=${userId}`);
        if (!favoritesResponse.ok) throw new Error("Erreur lors de la récupération des favoris.");

        const favoriteTeams = await favoritesResponse.json();

        if (favoriteTeams.length > 0) {
            // Si des équipes favorites existent, affichez-les
            allTeamsContainer.querySelector("h3").innerText = "Vos équipes favorites";

            favoriteTeams.forEach((team) => {
                const card = createTeamCard(team, true); // Création de carte avec bouton "Retirer des favoris"
                teamsContainer.appendChild(card);
            });
        } else {
            // Sinon, affichez toutes les équipes disponibles
            console.info("Aucune équipe favorite trouvée. Affichage de la liste des équipes.");
            const allTeamsResponse = await fetch(`http://localhost:8000/api/v1/teams/getAll`);
            if (!allTeamsResponse.ok) throw new Error("Erreur lors de la récupération des équipes.");

            const allTeams = await allTeamsResponse.json();
            allTeams.forEach((team) => {
                const card = createTeamCard(team, false); // Création de carte avec bouton "Ajouter aux favoris"
                teamsContainer.appendChild(card);
            });
        }

        // Afficher le conteneur des équipes
        allTeamsContainer.style.display = "block";

    } catch (error) {
        console.error("Erreur :", error);
        alert("Une erreur est survenue lors du chargement des équipes. Veuillez réessayer.");
    }
});

// Fonction pour créer une carte d'équipe
function createTeamCard(team, isFavorite) {
    const card = document.createElement("div");
    card.classList.add("card");

    card.innerHTML = `
        <img src="${team.img_path || 'https://via.placeholder.com/250x150'}" alt="Image de ${team.name}">
        <div class="card-body">
            <h4>${team.name}</h4>
            <p>Fondée en : ${team.founded || "N/A"}</p>
            <button data-team-id="${team.id}">
                ${isFavorite ? "Retirer des favoris" : "Ajouter aux favoris"}
            </button>
        </div>
    `;

    const button = card.querySelector("button");
    button.addEventListener("click", async () => {
        const teamId = button.getAttribute("data-team-id");
        if (isFavorite) {
            await removeFromFavorites(teamId);
            alert(`${team.name} a été retirée des favoris.`);
        } else {
            await addToFavorites(teamId);
            alert(`${team.name} a été ajoutée aux favoris.`);
        }
        location.reload(); // Rechargez la page pour mettre à jour les favoris après une modification
    });

    return card;
}

// Fonction pour ajouter une équipe aux favoris
async function addToFavorites(teamId) {
    const userId = localStorage.getItem("userId");
    if (!userId) {
        alert("Vous devez être connecté pour ajouter une équipe à vos favoris.");
        return;
    }

    try {
        const response = await fetch("http://localhost:8000/api/v1/users/favorite", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userId, team_id: teamId }),
        });
        if (!response.ok) throw new Error("Erreur lors de l'ajout aux favoris.");
        console.log(`Équipe avec ID ${teamId} ajoutée aux favoris.`);
    } catch (error) {
        console.error("Erreur :", error);
        alert("Impossible d'ajouter cette équipe aux favoris. Veuillez réessayer.");
    }
}

// Fonction pour retirer une équipe des favoris
async function removeFromFavorites(teamId) {
    const userId = localStorage.getItem("userId"); // Récupérer l'ID utilisateur du stockage local
    if (!userId) {
        alert("Vous devez être connecté pour retirer une équipe de vos favoris.");
        return;
    }

    try {
        // Inclure les paramètres user_id et team_id dans la query string de l'URL
        const response = await fetch(`http://localhost:8000/api/v1/users/favorite?user_id=${userId}&team_id=${teamId}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error("Erreur lors du retrait des favoris.");
        console.log(`Équipe avec ID ${teamId} retirée des favoris.`);
        alert("Équipe retirée des favoris avec succès !");
    } catch (error) {
        console.error("Erreur :", error);
        alert("Impossible de retirer cette équipe des favoris. Veuillez réessayer.");
    }
}