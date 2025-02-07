document.addEventListener("DOMContentLoaded", function () {
    fetchDataLastestMatches();
});

function fetchDataLastestMatches() {
    $.ajax({
        url: "http://localhost:8000/api/v1/results/latest-matches",
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayDataLatestMatches(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });
}

function displayDataLatestMatches(data) {
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
            window.location.href = `result.html?id=${item.id}`;
        });


        // Séparer les équipes
        const [team1, team2] = item.name.split(" vs ");

        // nom
        let team1Element = document.createElement("span");
        team1Element.textContent = team1;

        let team2Element = document.createElement("span");
        team2Element.textContent = team2;

        if (item.goal_set > item.goal_conceded) {
            team1Element.style.fontWeight = "bold";
        } else if (item.goal_conceded > item.goal_set) {
            team2Element.style.fontWeight = "bold";
        }

        const matchName = document.createElement("div");
        matchName.appendChild(team1Element);
        matchName.appendChild(document.createTextNode(" vs "));
        matchName.appendChild(team2Element);

        listItem.appendChild(matchName);

        //date
        const matchDate = document.createElement("div");
        matchDate.textContent = formatDate(item.starting_at);
        matchDate.style.fontSize = "14px";
        matchDate.style.color = "#808080";
        listItem.appendChild(matchDate);

        // Score
        const matchScore = document.createElement("div");

        const score1 = document.createElement("span");
        score1.textContent = item.goal_set;
        const score2 = document.createElement("span");
        score2.textContent = item.goal_conceded;

        if (item.goal_set > item.goal_conceded) {
            score1.style.fontWeight = "bold";
        } else if (item.goal_conceded > item.goal_set) {
            score2.style.fontWeight = "bold";
        }

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