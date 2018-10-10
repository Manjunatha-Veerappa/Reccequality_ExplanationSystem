let pieChart = document.getElementById('pieChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 16;
Chart.defaults.global.defaultFontColor = '#777';

let pieChartObj = new Chart(pieChart, {
    type:'pie',
    data: {
        labels: ['Good data', 'Bad data'],
        datasets: [{
            label: ['Amount of good data','Amount of Bad data'],
            data: [
                406,
                329
            ],
            backgroundColor: [
                'rgba(75, 192, 192, 0.6)',
                'rgba(255, 159, 64, 0.6)'
            ],
            hoverBorderColor:'#000'
        }]
    },
    options: {
        title:{
            display:true,
            text: 'Landfahrzeug dataset',
            fontSize: 24
        },
        legend:{
            display:true,
            position: 'bottom',
            labels:{
                fontColor: '#000'
            }
        },
        tooltips:{
            display: false
        }
    }
});