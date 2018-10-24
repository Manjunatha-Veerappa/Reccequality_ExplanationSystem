let getData = $.get('/luftfahrzeug_data')

getData.done(function(results){
    let pieChart = document.getElementById('barChart').getContext('2d');
    Chart.defaults.global.defaultFontFamily = 'Karla';
    Chart.defaults.global.defaultFontSize = 16;
    Chart.defaults.global.defaultFontColor = '#666';
    Chart.defaults.scale.ticks.beginAtZero = true;
    labels = (results.results[0])
    data = (results.results[1])

    let barChartData = {
        //labels: ['hochDecker', 'tragflachen_Stellung_Gerade', 'starrflugler', 'drehflugler_Triebwerk', 'drehflugler_Triebwerk_Luftauslass', 'drehflugler_Triebwerk_Lufteinlass', 'drehflugler_Heckausleger',
        //          'doppeldecker', 'drehflugler_Rotor_EinzelRotor_Rotorblatter', 'drehflugler', 'drehflugler_Rotor', 'abmessungen_Lange', 'drehflugler_Rumpf_Cockpit', 'drehflugler_Rumpf', 'triebwerke',
        //          'triebwerke_triebwerksart','leitwerk', 'rumpf', 'tragflachen', 'rumpf_Rumpfformen'],
        labels: labels,
        datasets: [{
            label: ['Data Quality'],
            data: data,
            backgroundColor: [
                'rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)',
                'rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)',
                'rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)',
                'rgba(75, 192, 192, 0.6)','rgba(75, 192, 192, 0.6)'
            ],
            hoverBorderColor:'#000'
        }]
    };

    let options = {
        title:{
            display:true,
            text: 'Explanation of the attributes',
            fontSize: 24
        },
        legend:{
            display:true,
            position: 'bottom',
            labels:{
                fontColor: '#000'
            }
        }
    };

    let barChartObj = new Chart(barChart, {
        type:'horizontalBar',
        data: barChartData,
        options: options
    });
});