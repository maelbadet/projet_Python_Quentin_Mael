document.addEventListener("DOMContentLoaded", async () => {
    const allTeamsContainer = document.getElementById("toutes-les-equipes");
    const teamsContainer = document.getElementById("teams-container"); // Conteneur pour les cartes

    try {
        const userId = localStorage.getItem("userId");
        if (!userId) {
            alert("Vous devez être connecté pour voir vos favoris.");
            return;
        }

        let favoriteTeams = [];
        try {
            // Appel pour récupérer les équipes favorites de l'utilisateur
            const favoritesResponse = await fetch(`http://localhost:8000/api/v1/users/favorites/getAllByUser?user_id=${userId}`);
            if (favoritesResponse.ok) {
                favoriteTeams = await favoritesResponse.json();
            } else if (favoritesResponse.status === 404) {
                // Pas de favoris trouvés, continuer pour récupérer toutes les équipes.
                console.info("Aucune équipe favorite trouvée. Affichage de la liste des équipes.");
            } else {
                throw new Error("Erreur inattendue lors de la récupération des favoris.");
            }
        } catch (error) {
            console.warn("Impossible de récupérer les favoris, récupération des équipes disponibles : ", error);
        }

        if (favoriteTeams.length > 0) {
            // Si des équipes favorites existent, affichez-les
            allTeamsContainer.querySelector("h3").innerText = "Vos équipes favorites";

            favoriteTeams.forEach((team) => {
                const card = createTeamCard(team, true); // Création de carte avec bouton "Retirer des favoris"
                teamsContainer.appendChild(card);
            });
        } else {
            // Sinon, affichez toutes les équipes disponibles
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
        } else {
            await addToFavorites(teamId);
        }
        location.reload(); // Rechargez la page pour mettre à jour les favoris après une modification
    });

    return card;
}

// Fonction pour ajouter une équipe aux favoris ou la restaurer si elle est "supprimée logiquement"
async function addToFavorites(teamId) {
    const userId = localStorage.getItem("userId");
    if (!userId) {
        alert("Vous devez être connecté pour ajouter une équipe à vos favoris.");
        return;
    }

    try {
        // Requête pour ajouter l'équipe aux favoris
        const response = await fetch("http://localhost:8000/api/v1/users/favorite", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: userId, team_id: teamId }),
        });

        // Si la requête POST réussit, équipe ajoutée
        if (response.ok) {
            console.log(`Équipe avec ID ${teamId} ajoutée aux favoris.`);
            return;
        }

        // Gestion du cas où l'équipe est déjà une favorite supprimée logiquement
        const errorData = await response.json();
        if (response.status === 400 && errorData.detail === "This team is already a favorite for this user.") {
            console.warn("L'équipe est déjà dans vos favoris. Tentative de restauration...");

            // Requête PATCH pour restaurer l'équipe supprimée logiquement
            const patchResponse = await fetch(`http://localhost:8000/api/v1/users/favorite?user_id=${userId}&team_id=${teamId}`, {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
            });

            if (patchResponse.ok) {
                console.log(`Équipe avec ID ${teamId} restaurée avec succès.`);
                return;
            }

            // Renvoyer une erreur si la restauration échoue
            throw new Error("Impossible de restaurer l'équipe comme favorite.");
        }

        // Renvoyer une erreur si une autre erreur inattendue survient
        throw new Error("Erreur lors de l'ajout aux favoris.");
    } catch (error) {
        console.error("Erreur :", error);
    }
}

// Fonction pour retirer une équipe des favoris
async function removeFromFavorites(teamId) {
    const userId = localStorage.getItem("userId"); // Récupérer l'ID utilisateur du stockage local
    if (!userId) {
        return;
    }

    try {
        const response = await fetch(`http://localhost:8000/api/v1/users/favorite?user_id=${userId}&team_id=${teamId}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error("Erreur lors du retrait des favoris.");
    } catch (error) {
        console.error("Erreur :", error);
    }
}