document.addEventListener("DOMContentLoaded", function () {
    fetchData();
});

function fetchData() {
    $.ajax({
        url: "http://localhost:8000/api/v1/leagues/getAll",
        method: "GET",
        dataType: "json",
        success: function (data) {
            displayData(data);
        },
        error: function (error) {
            console.error("Erreur AJAX :", error);
        }
    });
}

function displayData(data) {
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
