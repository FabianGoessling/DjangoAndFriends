function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    console.log('hello again')
    var newElement = $(selector).clone(true);
    console.log(newElement)
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    console.log(total)
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function () {
        console.log($(this))
        var name = $(this).attr('name').replace('-' + (total - 1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({ 'name': name, 'id': id }).val('').removeAttr('checked');
    });
    newElement.find('label').each(function () {
        var forValue = $(this).attr('for');
        if (forValue) {
            forValue = forValue.replace('-' + (total - 1) + '-', '-' + total + '-');
            $(this).attr({ 'for': forValue });
        }
    });
    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var conditionRow = $('.form-row:not(:last)');
    conditionRow.find('.btn.add-form-row')
        .removeClass('btn-success').addClass('btn-danger')
        .removeClass('add-form-row').addClass('remove-form-row')
        .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
    return false;
}
function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1) {
        btn.closest('.form-row').remove();
        var forms = $('.form-row');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i = 0, formCount = forms.length; i < formCount; i++) {
            $(forms.get(i)).find(':input').each(function () {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}

$(document).on('click', '.add-form-row', function (e) {
    console.log('hello')
    e.preventDefault();
    cloneMore('.form-row:last', 'site_set');
    return false;
});

$(document).on('click', '.remove-form-row', function (e) {
    e.preventDefault();
    deleteForm('form', $(this));
    return false;
});

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