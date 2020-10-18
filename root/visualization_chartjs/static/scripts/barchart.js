var $populationChart = $("#population-chart");
var ctx = $populationChart[0].getContext("2d");

var mychart =  new Chart(ctx, {
            type: 'bar',
            data: {
              labels: [],
              datasets: [{
                label: 'Population',
                backgroundColor: 'blue',
                data: []
              }]
            },
            options: {
              responsive: true,
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Population Bar Chart'
              }
            }
          });

// var csrftoken = $("[name=csrfmiddlewaretoken]").val();
//
//     var getData = function() {
//       $.ajax({
//         url: $populationChart.data("url"),
//           type: "POST",
//   headers:{
//         "X-CSRFToken": csrftoken
//     },       success: function (data) {
//           mychart.data.labels = data.labels;
//           mychart.data.datasets[0].data = data.data;
//           mychart.data.datasets[0].backgroundColor = data.color;
//           mychart.update();
//           console.log(data);
//           }
//       });
//
//     };
    // get new data every 3 seconds
//setInterval(getData, 10000);

