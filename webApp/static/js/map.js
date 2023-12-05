class map {

    CESI = {
        lat: 44.865154,
        lng: -0.577127
    }
    zoom = 25
    map = L.map('map').setView([this.CESI.lat, this.CESI.lng], this.zoom)

    constructor() {
        this.init()
        this.clickEvent = new Event("mapClicked")
    }

    init() {

        let mainLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        });

        mainLayer.addTo(this.map);

        this.map.on('click', function () {
            this.dispatchEvent(this.clickEvent)
        })

    }

    listenEvent(callback) {
        this.addEventListener('mapClicked', callback);
    }
    
    addPoint(lat, long) {
        let marker = L.marker([lat, long])
        
        marker.addTo(this.map)
    }

    onMapClick(e) {
        alert('You clicked here : '+e.latlng)
    }   

}

const myMap = new map();