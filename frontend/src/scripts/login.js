document.getElementById('login-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    };

    try {
        console.log(formData);
        // Appel AJAX vers l'API de connexion
        const response = await fetch('http://localhost:8000/api/v1/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const result = await response.json();
            localStorage.setItem('userId', result.id);
            localStorage.setItem('userName', `${result.name}`);
            window.location.href = '/';
        } else {
            const errorResult = await response.json();
            alert(`Erreur: ${errorResult.detail}`);
        }
    } catch (error) {
        console.error('Erreur lors de l’appel à l’API:', error);
        alert("Une erreur s'est produite. Veuillez réessayer.");
    }
});