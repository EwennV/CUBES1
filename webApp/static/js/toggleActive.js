function toggleActive(id) {
    fetch('http://127.0.0.1:8000/api/sensor/toggle', {
        method: "PUT",
        body: JSON.stringify({
            id: id
        })
    }).then(response => {
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