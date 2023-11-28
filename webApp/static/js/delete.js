document.getElementById('deleteButton').addEventListener('click', function() {
    const idValue = document.getElementById('idInput').value;

    fetch('/api/sensor/delete/' + idValue + '/')
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        })
        .catch(error => {
            console.error('Erreur lors de la suppression du capteur:', error);
        });
});
