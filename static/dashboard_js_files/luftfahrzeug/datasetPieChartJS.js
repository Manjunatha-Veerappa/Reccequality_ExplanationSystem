let pieChart = document.getElementById('pieChart').getContext('2d');

Chart.defaults.global.defaultFontFamily = 'Karla';
Chart.defaults.global.defaultFontSize = 16;
Chart.defaults.global.defaultFontColor = '#666';

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
     },
    onClick:function(e){
        var activePoints = pieChartObj.getElementsAtEvent(e);
        var selectedIndex = activePoints[0]._index;
        if(selectedIndex == 0){
            console.log('Good data has been selected')
            $.ajax({
               url:"/static/classification_csv_files/LuftfahrzeugClassificationCategorical.csv",
               dataType:"text",
               success:function(data)
               {
                var resultCount = 0;
                var classification_data = data.split(/\r?\n|\r/);
                var table_data = '<table class="table table-bordered table-striped">';
                for(var count = 0; count<classification_data.length; count++)
                {
                 var cell_data = classification_data[count].split(",");
                 table_data += '<tr>';
                 for(var cell_count=0; cell_count<cell_data.length; cell_count++)
                 {
                  if(count === 0)
                  {
                   table_data += '<th>'+cell_data[cell_count]+'</th>';
                  }
                  else
                  {
                    if(cell_data[cell_data.length - 1] == 1){
                        //cell_data[cell_count].cells[0].backgroundColor = "#c1c1c1";
                        table_data += '<td>'+cell_data[cell_count]+'</td>';
                    }
                  }
                 }
                 table_data += '</tr>';
                }
                table_data += '</table>';
                $('#data_table').html(table_data);
               }

            });
        }
        else{
            console.log('Bad data has been selected')
            $.ajax({
               url:"/static/classification_csv_files/LuftfahrzeugClassificationCategorical.csv",
               dataType:"text",
               success:function(data)
               {
                var resultCount = 0;
                var classification_data = data.split(/\r?\n|\r/);
                var table_data = '<table class="table table-bordered table-striped">';
                for(var count = 0; count<classification_data.length; count++)
                {
                 var cell_data = classification_data[count].split(",");
                 table_data += '<tr>';
                 for(var cell_count=0; cell_count<cell_data.length; cell_count++)
                 {
                  if(count === 0)
                  {
                   table_data += '<th>'+cell_data[cell_count]+'</th>';
                  }
                  else
                  {
                    if(cell_data[cell_data.length - 1] == 0){
                        //Abmessungen Länge exception
                        if(cell_data[1] == -1 && cell_count == 1){
                            table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                        }
                        //Starrflugler exception
                        else if(cell_data[2] == 0 && (cell_count == 3 || cell_count == 4 || cell_count == 5 || cell_count == 6)){
                            if(cell_data[3] != 0 && cell_count == 3){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[4] != 0 && cell_count == 4){
                                table_data += '<td style="color:red"">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[5] != 0 && cell_count == 5){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[6] != 0 && cell_count == 6){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        //DoppelDecker exception
                        else if(cell_data[9] == 0 && cell_count == 10){
                            if(cell_data[10] != 0 && cell_count == 10){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        //Drehflugler exception
                        else if(cell_data[7] == 0 && cell_count == 8){
                            if(cell_data[8] != 0 && cell_count == 8){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        //Drehflugler exception (additional)
                        else if(cell_data[7] == 0 && (cell_count == 7 || cell_count == 14 || cell_count == 15 || cell_count == 16 || cell_count == 17)){
                            if(cell_data[14] != 0 && cell_count == 14){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[15] != 0 && cell_count == 15){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[16] != 0 && cell_count == 16){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[17] != 0 && cell_count == 17){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        //Hochdecker exception
                        else if(cell_data[11] == 0 && (cell_count == 11 || cell_count == 3 || cell_count == 12 || cell_count == 13)){
                            if(cell_data[3] != 0 && cell_count == 3){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[12] != 0 && cell_count == 12){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else if(cell_data[13] != 0 && cell_count == 13){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        //Lufteinlass exception
                        else if(cell_data[18] == 0 && cell_count == 19){
                            if(cell_data[19] != 0 && cell_count == 19){
                                table_data += '<td style="color:red">'+cell_data[cell_count]+'</td>';
                            }
                            else{
                                table_data += '<td>'+cell_data[cell_count]+'</td>';
                            }
                        }
                        else{
                            table_data += '<td>'+cell_data[cell_count]+'</td>';
                        }

                    }
                  }
                 }
                 table_data += '</tr>';
                }
                table_data += '</table>';
                $('#data_table').html(table_data);
               }

            });
        }
    }
};

let pieChartObj = new Chart(pieChart, {
    type:'pie',
    data: pieChartData,
    options: options
});