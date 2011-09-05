function updateCheckboxes(checkbox) {
    if (checkbox.checked) {
        $('#supercheckbox').attr('checked', true);
        $('.massaction').removeClass('disabled');
    } else {
        var checked = 0;
        $('.list_item').each(function() {
            if (this.checked) {
                checked++;
            }
        });
        if (checked == 0) {
            $('#supercheckbox').attr('checked', false);
            $('.massaction').addClass('disabled');
        }
    }
}

function updateAllCheckboxes(checkbox) {
    $('.list_item').attr('checked', checkbox.checked);
    if (checkbox.checked) {
        $('.massaction').removeClass('disabled');
    } else {
        $('.massaction').addClass('disabled');
    }
}
