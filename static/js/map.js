class map {

    CESI = {
        lat: 44.865154,
        lng: -0.577127
    }
    zoom = 25
    map = L.map('map').setView([this.CESI.lat, this.CESI.lng], this.zoom)

    constructor() {
        this.init()
    }

    init() {

        let mainLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        });

        mainLayer.addTo(this.map);
    }
    
    addPoint(lat, long) {
        L.marker([lat, long]).addTo(this.map)
    }
}