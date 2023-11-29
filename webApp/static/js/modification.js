function submitSensor() {
    const nameValue = document.getElementById('nameInput').value;
    const idValue = document.getElementById('idInput').getAttribute('data-sensor-id');

    fetch("http://localhost:8000/api/sensor/update", {
    method: "PUT",
    body: JSON.stringify({
        id: idValue,
        name: nameValue,
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Faites quelque chose avec les données renvoyées par le serveur
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
document.getElementById('submit').addEventListener('click',function(event) {
    event.preventDefault();
    submitSensor();
})