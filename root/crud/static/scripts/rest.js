// Hook on the submit button
$(document).on("submit", ".js_form", function () {
    console.log('HAAAALLLOOO')
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                alert("Book created!");
                $("#table_input").html(data.book_table);  // <-- This is just a placeholder for now for testing
            }
            else {
                $("#table_input").html(data.book_table);
            }
        }
    });
    return false; // avoid a full POST request
});