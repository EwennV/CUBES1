function getSensorName(id) {
    fetch('http://localhost:8000/api/sensor?id='+id)
}