function submitAlert() {
    const tinfValue = document.getElementById('tinfInput').value;
    const tsupValue = document.getElementById('tsupInput').value;
    const hinfValue = document.getElementById('hinfInput').value;
    const hsupValue = document.getElementById('hsupInput').value;
    const frequencyValue = document.getElementById('frequencyInput').value;
    const mailValue = (document.getElementById('mailInput').value).split(',');
    const idValue = document.getElementById('idInput').getAttribute('alert-id');


    fetch("http://localhost:8000/api/alert/update", {
    method: "PUT",
    body: JSON.stringify({
        id: idValue,
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