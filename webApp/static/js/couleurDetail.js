document.addEventListener("DOMContentLoaded", function () {
    var temperatureValue = parseFloat(document.getElementById("detail_temp").innerText);

    var detailTemp = document.getElementById("detail_temp");
    if (temperatureValue < 10) {
        detailTemp.classList.add("low-temperature");
    } else if (temperatureValue >= 10 && temperatureValue <= 20) {
        detailTemp.classList.add("normal-temperature");
    } else {
        detailTemp.classList.add("high-temperature");
    }
});