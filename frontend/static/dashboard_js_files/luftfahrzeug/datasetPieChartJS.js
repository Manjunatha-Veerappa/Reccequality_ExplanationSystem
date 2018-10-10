let pieChart = document.getElementById('pieChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 16;
Chart.defaults.global.defaultFontColor = '#777';

let pieChartData = {
    labels: ['Good data', 'Bad data'],
    datasets: [{
        label: ['Amount of good data','Amount of Bad data'],
        data: [200, 385],
        backgroundColor: [
            'rgba(75, 192, 192, 0.6)',
            'rgba(255, 159, 64, 0.6)'
        ],
        hoverBorderColor:'#000'
    }]
};

let options = {
    title:{
        display:true,
        text: 'Luftfahrzeug dataset',
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
        display: true,
        callbacks: {
            label: function(tooltipItem, data) {
              //get the concerned dataset
              var dataset = data.datasets[tooltipItem.datasetIndex];
              //calculate the total of this data set
              var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                return previousValue + currentValue;
              });
              //get the current items value
              var currentValue = dataset.data[tooltipItem.index];
              //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
              var percentage = Math.floor(((currentValue/total) * 100)+0.5);

              return percentage + "% - " + currentValue + " vectors";
            }
         }
     }
};

let pieChartObj = new Chart(pieChart, {
    type:'pie',
    data: pieChartData,
    options: options
});