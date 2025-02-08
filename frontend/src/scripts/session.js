document.addEventListener("DOMContentLoaded", () => {
    const loginLink = document.getElementById("login-link");
    const welcomeLink = document.getElementById("welcome-link");
    const userNameSpan = document.getElementById("user-name");

    // Vérification de la session (via localStorage)
    const userId = localStorage.getItem("userId");
    const userName = localStorage.getItem("userName");

    if (userId && userName) {
        // Si l'utilisateur est connecté (userId existe dans localStorage)
        loginLink.style.display = "none";
        userNameSpan.textContent = userName;
        welcomeLink.style.display = "inline";
    } else {
        // Si aucun utilisateur connecté
        loginLink.style.display = "inline";
        welcomeLink.style.display = "none";
    }
});