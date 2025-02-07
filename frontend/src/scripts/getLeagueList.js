document.addEventListener("DOMContentLoaded", function () {
    fetchDataGetAll();
});

function fetchDataGetAll() {
    /*$.ajax({
        url: "http://localhost:8000/api/v1/leagues/getAll",
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayDataGetAll(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });*/
    displayDataGetAll([
        {
            "id": 1,
            "name": "Premiership",
            "country_id": 1161,
            "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/501.png"
        }
    ])
}

function displayDataGetAll(data) {
    console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",data);
    const listContainer = document.getElementById("list");
    listContainer.innerHTML = "";

    data.forEach(item => {
        const listItem = document.createElement("li");

        const img = document.createElement("img");
        img.src = item.image_path;
        img.alt = item.name;

        const name = document.createElement("span");
        name.textContent = item.name;

        listItem.appendChild(img);
        listItem.appendChild(name);
        listContainer.appendChild(listItem);
    });
}
