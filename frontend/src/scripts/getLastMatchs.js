document.addEventListener("DOMContentLoaded", function () {
    fetchDataLastestMatches();
});

function fetchDataLastestMatches() {
    /*$.ajax({
        url: "http://localhost:8000/api/v1/results/latest-matches",
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayDataLastestMatches(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });*/
    displayDataLatestMatches([
        {
            "id": 228,
            "name": "Celtic vs Hearts",
            "season_id": 825,
            "starting_at": "2017-05-21",
            "goal_conceded": 0,
            "goal_set": 2
        },
        {
            "id": 224,
            "name": "St. Johnstone vs Rangers",
            "season_id": 825,
            "starting_at": "2017-05-21",
            "goal_conceded": 2,
            "goal_set": 1
        },
        {
            "id": 226,
            "name": "Partick Thistle vs Aberdeen",
            "season_id": 825,
            "starting_at": "2017-05-21",
            "goal_conceded": 6,
            "goal_set": 0
        },
        {
            "id": 223,
            "name": "Hamilton Academical vs Dundee",
            "season_id": 825,
            "starting_at": "2017-05-20",
            "goal_conceded": 0,
            "goal_set": 4
        }
    ])
}

function displayDataLatestMatches(data) {
    console.log("Match Data:", data);
    const listContainer = document.getElementById("listLastMatch");

    if (!listContainer) {
        console.error("Element #listLastMatch not found!");
        return;
    }

    listContainer.innerHTML = "";

    data.forEach(item => {
        const listItem = document.createElement("li");
        listItem.style.cursor = "pointer";
        listItem.addEventListener("click", () => {
            //window.location.href = `match-details.html?id=${item.id}`;
            window.location.href = `result.html?id=${item.id}`;
        });


        // Séparer les équipes
        const [team1, team2] = item.name.split(" vs ");

        // Déterminer l'équipe gagnante
        let team1Element = document.createElement("span");
        team1Element.textContent = team1;

        let team2Element = document.createElement("span");
        team2Element.textContent = team2;

        if (item.goal_set > item.goal_conceded) {
            team1Element.style.fontWeight = "bold"; // Mettre en gras l'équipe qui a marqué le plus
        } else if (item.goal_conceded > item.goal_set) {
            team2Element.style.fontWeight = "bold"; // Mettre en gras l'autre équipe si elle a gagné
        }

        const matchName = document.createElement("div");
        matchName.appendChild(team1Element);
        matchName.appendChild(document.createTextNode(" vs "));
        matchName.appendChild(team2Element);

        listItem.appendChild(matchName);

        // Date du match (formatée)
        const matchDate = document.createElement("div");
        matchDate.textContent = formatDate(item.starting_at);
        matchDate.style.fontSize = "14px"; // Optionnel : réduire la taille du texte
        matchDate.style.color = "#808080"; // Optionnel : couleur grise pour la date
        listItem.appendChild(matchDate);

        // Score du match
        const matchScore = document.createElement("div");

        const score1 = document.createElement("span");
        score1.textContent = item.goal_set;
        const score2 = document.createElement("span");
        score2.textContent = item.goal_conceded;

        // Appliquer le style gras au score le plus élevé
        if (item.goal_set > item.goal_conceded) {
            score1.style.fontWeight = "bold";
        } else if (item.goal_conceded > item.goal_set) {
            score2.style.fontWeight = "bold";
        }

        // Ajouter le score formaté
        matchScore.appendChild(score1);
        matchScore.appendChild(document.createTextNode(" - "));
        matchScore.appendChild(score2);
        listItem.appendChild(matchScore);

        // Ajouter à la liste
        listContainer.appendChild(listItem);
    });
}

// Fonction pour formater la date
function formatDate(dateString) {
    const options = { year: "numeric", month: "long", day: "numeric" };
    return new Date(dateString).toLocaleDateString("fr-FR", options);
}