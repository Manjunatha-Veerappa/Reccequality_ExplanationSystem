$(document).ready(function(){

  console.log("Schiffe");

  $.ajax({
   url:"/static/classification_files/SchiffeClassificationCategorical.csv",
   dataType:"text",
   success:function(data)
   {
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
       table_data += '<td>'+cell_data[cell_count]+'</td>';
      }
     }
     table_data += '</tr>';
    }
    table_data += '</table>';
    $('#classification_table').html(table_data);
   }

 });

});