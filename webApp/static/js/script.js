const barCanvas = document.getElementById('barCanvas');
const barChart = new Chart(barCanvas, {
    type: 'bar',
    data: {
        labels: ['date', 'date', 'date', 'date', 'date', 'date'],
        datasets: [{
            label: 'humidité',
            data: [22, 19, 23, 27, 24, 21],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
        }
});

const tempCanvas = document.getElementById('tempCanvas');
const tempChart = new Chart(tempCanvas, {
    type: 'line',  
    data: {
        labels: ['date', 'date', 'date', 'date', 'date', 'date'],
        datasets: [{
            label: 'température',
            data: [22, 19, 23, 27, 24, 21],
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});