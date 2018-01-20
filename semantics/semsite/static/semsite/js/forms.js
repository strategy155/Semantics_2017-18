/**
 * Created by geoolekom on 08.01.18.
 */

function ajaxSubmitAction (event) {
    var currentForm = $(this);
    event.preventDefault();
    var formData = new FormData(currentForm[0]);
    $.ajax({
        url: currentForm.attr('action'),
        method: currentForm.attr('method'),
        data: formData,
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        cache: false
    }).done(function (response) {
        currentForm.trigger(currentForm.data('success-event') || 'default-success-event', response);
        currentForm.trigger('reset');
    }).fail(function (xhr) {
        const response = xhr.responseJSON;
        for (var err in response.errors) {
            var elem = currentForm.find('.form-error.' + err);
            elem.html('');
            $.each(response.errors[err], function (idx, value) {
                elem.append(value);
            });
        }
    });
}

function processSelector(selector) {
    selector.submit(ajaxSubmitAction);

    selector.find(':input').keydown(function () {
        var fieldName = $(this).attr('name');
        $(this).closest('.ajax-form').find('.form-error.' + fieldName).html('');
    });
}

function processAjaxForms() {
    processSelector($('.ajax-form'));
}

$(document).ready(function () {
    processAjaxForms();
    // $('input[name="phone"]').mask('+7-999-999-99-99', {placeholder:'_'});
});