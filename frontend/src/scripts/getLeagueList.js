document.addEventListener("DOMContentLoaded", function () {
    fetchDataGetAll();
});

function fetchDataGetAll() {
    $.ajax({
        url: "http://localhost:8000/api/v1/leagues/getAll",
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayDataGetAll(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });
}

function displayDataGetAll(data) {
    const listContainer = document.getElementById("listLeague");
    listContainer.innerHTML = "";

    data.forEach(item => {
        const listItem = document.createElement("li");

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
