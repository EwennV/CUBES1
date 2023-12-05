function submitSensor() {
    const tinfValue = document.getElementById('tinfInput').value;
    const tsupValue = document.getElementById('tsupInput').value;
    const hinfValue = document.getElementById('hinfInput').value;
    const hsupValue = document.getElementById('hsupInput').value;
    const frequencyValue = document.getElementById('frequencyInput').value;
    const mailValue = (document.getElementById('mailInput').value).split(',');

    fetch("http://localhost:8000/api/sensor/update", {
    method: "PUT",
    body: JSON.stringify({
        frequency: frequencyValue,
        temperature_inferior: tinfValue,
        temperature_superior: tsupValue,
        humidity_inferior: hinfValue,
        humidity_superior: hsupValue,
        recipients: mailValue
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