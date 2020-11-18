// Get Django csrf Token
var csrftoken = $("[name=csrfmiddlewaretoken]").val();

document.body.addEventListener('click', function (event) {
    if (event.target.id === 'ajaxbutton') {
        const form = event.target.form;
        const data = new FormData(form);
        $.ajax({
            url: form.action,
            type: form.method,
            headers: {
                "X-CSRFToken": csrftoken,
                "contentType": "application/x-www-form-urlencoded"
            },
            data: data,
            processData: false,
            contentType: false,
            success: function (data) {
                console.log(table.getData())
                console.log(jExcelExtensions.convertJSONdata(data))
                table.setData(jExcelExtensions.convertJSONdata(data))
                console.log(data);
                console.log(table.getData())
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
        time = 3250 + (1000 * i);
        setTimeout(function () {
            $(elem).fadeOut("slow");
        }, time);
    }
}

// Simulate a click on radio-button so that it loads demographic content
var data = [
    [0.3, 10, "=B1*C1"],
    [0.3, 5, "=B2*C2"],
    [0.4, 5, "=B3*C3"],
];

// A custom method to SUM all the cells in the current column

var SUMCOL = function(instance, columnId) {
    var total = 0;
    for (var j = 0; j < instance.options.data.length; j++) {
        if (Number(instance.records[j][columnId-1].innerHTML)) {
            total += Number(instance.records[j][columnId-1].innerHTML);
        }
    }
    return total;
}

var table = jexcel(document.getElementById('spreadsheet'), {
    data:data,
    minDimensions: [4,5],
    tableOverflow:false,
    columnDrag:true,
    footers: [['=SUMCOL(TABLE(), COLUMN())','=SUMCOL(TABLE(), COLUMN())','=SUMCOL(TABLE(), COLUMN())']],
    columns: [
        { type: 'numeric', title:'Weight', width:120 },
        { type: 'dropdown', title:'Asset', width:200, source:[ "Apple", "Microsoft", "Amazon" ] },
        { type: 'calendar', title:'Date', width:200 },
    ]
});

var jExcelExtensions = {
    convertJSONdata : function (jsn) {
        console.log(jsn)
        var jArray = new Array(), i = 0, prop;
        console.log(Object.keys( jsn ).length)
        for (i = 0; i < Object.keys( jsn ).length; i++) {
 	    var v = new Array();
            for (prop in jsn[i]) {
                if (jsn[i].hasOwnProperty(prop)) {
                    console.log(jsn[i][prop])
                    if (typeof jsn[i][prop] === "string") {
                        v.push('"' + jsn[i][prop] + '"');
                    }
                    else {
                        v.push(jsn[i][prop]);
                    }
                }
            }
            jArray.push('[' + v + ']');
        }
        return '[' + jArray + ']';
    },
}