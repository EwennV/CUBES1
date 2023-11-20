function init () {
    const CESI = {
        lat: 44.865154,
        lng: -0.577127
    }

    const zoom = 25
    const map = L.map('map').setView([CESI.lat, CESI.lng], zoom)
    
    const mainLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    mainLayer.addTo(map);
}

init()