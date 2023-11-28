document.getElementById('deleteButton').addEventListener('onclick', function() {
    var sensorId = document.getElementById('inputId');

    // Effectuez la requête vers le backend Django
    fetch('/api/sensor/delete/?sensor_id=' + sensorId)
        .then(response => response.json())
        .then(data => {
            console.log(data.message);  // Faites quelque chose avec la réponse du serveur
        })
        .catch(error => {
            console.error('Erreur lors de la suppression du capteur:', error);
        });
});
