document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);

    const id = urlParams.get("id");

    console.log("ID récupéré :", id);
    fetchDataGetLeagueInfo(id);
});

function fetchDataGetLeagueInfo(id) {
    $.ajax({
        url: `http://localhost:8000/api/v1/leagues/get/${id}`,
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayDataGetLeagueInfo(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });
}

function displayDataGetLeagueInfo(data) {
    console.log('data du get info league',data);
    const listContainer = document.getElementById("listLeague");
    listContainer.innerHTML = "";

    data.forEach(item => {
        const listItem = document.createElement("li");
        listItem.style.cursor = "pointer";
        listItem.addEventListener("click", () => {
            window.location.href = `league.html?id=${item.id}`;
        });

        const img = document.createElement("img");
        img.src = item.image_path;
        img.alt = item.name;

        const name = document.createElement("span");
        name.textContent = item.name;

        const leagueItem = document.createElement("div");
        leagueItem.classList.add("leagueItem");
        leagueItem.appendChild(img);
        leagueItem.appendChild(name);
        listItem.appendChild(leagueItem)
        listContainer.appendChild(listItem);
    });
}
