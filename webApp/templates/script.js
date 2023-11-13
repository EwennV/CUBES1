const ctx = document.getElementsByClassName('myChart');
      
new Chart(ctx, {
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