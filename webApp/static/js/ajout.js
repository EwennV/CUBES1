function submitSensor() {
    const idValue = document.getElementById('idInput').value;
    const nameValue = document.getElementById('nameInput').value;
    const latitudeValue = document.getElementById('latitudeInput').value;
    const longitudeValue = document.getElementById('longitudeInput').value;

    fetch("http://localhost:8000/api/sensor/create", {
    method: "POST",
    body: JSON.stringify({
        id: idValue,
        name: nameValue,
        lat: latitudeValue,
        lng: longitudeValue
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if (data.message) {
            cuteToast({
                type: "success",
                title: "Succès",
                message: data.message
            })
            setTimeout(() => {
                location.reload()
            }, 2000);
        } else {
            cuteToast({
                type: "error",
                title: "Erreur",
                message: data.error
            })
        }
    })
    .catch(error => {
        console.log(error)
        cuteToast({
            type: "error",
            title: "Erreur",
            message: "Une erreur est survenue"
        })
    });
}
document.getElementById('submit').addEventListener('onclick',function(event) {
    event.preventDefault();
    submitSensor();
})