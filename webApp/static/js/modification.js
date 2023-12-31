function submitSensor() {
    const nameValue = document.getElementById('nameInput').value;
    const idValue = document.getElementById('idInput').getAttribute('data-sensor-id');
    const lat = document.getElementById('lat').value;
    const lng = document.getElementById('lng').value;

    fetch("http://localhost:8000/api/sensor/update", {
    method: "PUT",
    body: JSON.stringify({
        id: idValue,
        name: nameValue,
        lat: lat,
        lng: lng
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