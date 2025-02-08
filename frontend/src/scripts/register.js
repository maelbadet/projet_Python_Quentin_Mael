document.getElementById('register-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // Empêche le rechargement de la page

    // Récupération des données du formulaire
    const formData = {
        name: document.getElementById('name').value,
        surname: document.getElementById('surname').value,
        email: document.getElementById('email').value,
        telephone: document.getElementById('telephone').value,
        password: document.getElementById('password').value
    };

    try {
        // Appel AJAX vers l'API
        const response = await fetch('http://localhost:8000/api/v1/users/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const result = await response.json();
            localStorage.setItem('userId', result.id);
            window.location.href = 'connexion.html';
        } else {
            const errorResult = await response.json();
            alert(`Erreur: ${errorResult.detail || 'Échec de l’inscription.'}`);
        }
    } catch (error) {
        console.error('Erreur lors de l’appel à l’API:', error);
        alert("Une erreur s'est produite. Veuillez réessayer.");
    }
});