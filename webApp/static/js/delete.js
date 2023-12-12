function deleteSensor() {
    const idValue = document.getElementById('idInput').getAttribute('data-sensor-id');

    fetch(`http://localhost:8000/api/sensor/delete?id=${idValue}`, {
    method: "DELETE",
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
                window.location.href = "htpp://127.0.0.1/dashboard/"
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