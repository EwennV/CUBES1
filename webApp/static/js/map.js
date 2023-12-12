class map {

    CESI = {
        lat: 44.865154,
        lng: -0.577127
    }

    zoom = 25

    map = L.map('map', {
    }).setView(
        [this.CESI.lat, this.CESI.lng],
        this.zoom
    )

    catFound = new CustomEvent("animalfound", {
        detail: {
          name: "cat",
        },
    });

    constructor() {
        this.init()
    }

    init() {

        let mainLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        });

        mainLayer.addTo(this.map);
    }

    listenEvent(callback) {
        this.map.on('click', callback)
    }
    
    addPoint(lat, long) {
        let marker = L.marker([lat, long])
        
        marker.addTo(this.map)
        return marker
    }

    onMapClick(e) {
        console.log('You clicked zzzzzzzz : '+e.latlng)
    }   

}

const myMap = new map();