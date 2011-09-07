var CreateRecordForm = new function() {

    this.submit = function() {
        jQuery("#add_form").submit();
    };

    this.cancel = function() {
        hide_create_window();
    };
};

var CreateRecordWindow = new function() {

    this.submit = function() {
        jQuery("#add_form").submit();
    };

    this.cancel = function() {
        hide_create_window();
    };
};

var Grid = new function() {

    this.doMassAction = function (element) {
        button = jQuery(element);

        if (button.hasClass('disabled')) {
            return false;
        }

        this.setupActiveButton(button);
        this.blockToolbarButtons();

        jQuery('#recordset_action').value = element.id;
        jQuery('#recordset').submit();
    };

    this.massActionError = function() {
        this.restoreActiveButton();
        this.releaseToolbarButtons();

        alert('error');
    };

    this.massActionSuccess = function() {
        this.restoreActiveButton();
        this.releaseToolbarButtons();

        alert('success');
    };

    this.setupActiveButton = function(button) {
        button.addClass('toolbar_ajax_blocker');
        button.html('Sending...');
    };

    this.restoreActiveButton = function() {
        jQuery('.toolbar_ajax_blocker').each(function() {
            jQuery(this).html(this.title);
        });
    };

    this.blockToolbarButtons = function() {
        jQuery('.toolbarbtn').each(function() {
            button = jQuery(this);
            if (!button.hasClass('disabled')) {
                button.addClass('toolbar_ajax_block');
                button.addClass('disabled');
            }
        });
    };

    this.releaseToolbarButtons = function() {
        jQuery('.toolbarbtn').each(function() {
            button = jQuery(this);
            if (button.hasClass('toolbar_ajax_block')) {
                button.removeClass('toolbar_ajax_block');
                button.removeClass('disabled');
            }
        });
    };
};

//function do_submit() {
//    jQuery("#add_form").submit();
//}
//
//function do_cancel() {
//    hide_create_window();
//}

function hide_create_window() {
    jQuery('#create_form').hide();
}

function enable_window_buttons() {
    jQuery("#save_button").removeClass('disabled');
    jQuery("#cancel_button").removeClass('disabled');
    jQuery("#save_button").html('Save');
}

function disable_window_buttons() {
    jQuery("#save_button").addClass('disabled');
    jQuery("#cancel_button").addClass('disabled');
    jQuery("#save_button").html('Sending...');
}

function reload_grid() {
    //.load can't handle http errors???
    jQuery("#records_list").load(url_load_grid + '?ajax=1');
}

function send_add_request(e){
    disable_window_buttons();

    e.preventDefault();
    var form = jQuery(e.target);
    jQuery.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: form.serialize(),
        dataType: 'json',
        success: add_success,
        error: add_error
    });
}

function add_success(json) {
    reload_grid();
    hide_create_window();
    enable_window_buttons();
    show_success('Record succesfully added', 5000);
}

function add_error(xhr, ajaxOptions, thrownError) {
    enable_window_buttons();
}

function showCreateDialog(id) {
    $('#success_message').hide();
    $('#modal_body').load(url_record_add);
    $(id).show();
}

function editRecord(id) {
    showCreateDialog('#create_form');
}

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

function submitGridMassAction(e){
    e.preventDefault();
    var form = jQuery(e.target);
    jQuery.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: form.serialize(),
        dataType: 'json',
        success: function() {alert('success');},
        error: Grid.massActionError()
    });
}

function show_success(message, autohide_timeout) {
    $('#success_message_body').html(message);
    $('#success_message').show();

    if (autohide_timeout) {
        setTimeout(hide_success, autohide_timeout);
    }
}

function hide_success() {
    $('#success_message').hide();
}
