// form dynamic request for charts
var csrftoken = $("[name=csrfmiddlewaretoken]").val();

document.body.addEventListener( 'click', function (event) {
    if( event.target.className === 'form-check-input dataset' ) {
        const form = event.target.form;
        const data = new FormData(form);
        $.ajax({
        url: form.action,
        type: form.method,
        headers:{"X-CSRFToken": csrftoken,
                 "contentType": "application/x-www-form-urlencoded"},
        data: data,
        processData: false,
        contentType: false,
      success: function (data) {
          mychart.data.labels = data.labels;
          mychart.data.datasets[0].data = data.data;
          mychart.data.datasets[0].backgroundColor = data.color;
          mychart.update();
          console.log(data);
          }
      });
    }
});


// fade out message alerts
function fade_alerts() {
    alerts = document.getElementsByClassName("alert msg");
        var i = alerts.length;
        for (let elem of alerts) {
            i--;
            time = 3250+(1000*i);
            setTimeout(function() {
                $(elem).fadeOut("slow");
            }, time);
        }
}

// Simulate a click on radio-button so that it loads demographic content
var hatEvalData = document.getElementById("dataset_a");
hatEvalData.click();