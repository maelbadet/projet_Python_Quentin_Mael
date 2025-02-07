document.addEventListener("DOMContentLoaded", function () {
    fetchData();
});

function fetchData() {
    $.ajax({
        url: "http://localhost:8000/api/v1/results/latest-matches",
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
    console.log("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",data);
    const listContainer = document.getElementById("listLastMatch");
    listContainer.innerHTML = "";

    data.forEach(item => {
        const listItem = document.createElement("li");

        const name = document.createElement("a");
        name.textContent = item.name;

        listItem.appendChild(name);
        listContainer.appendChild(listItem);
    });
}
