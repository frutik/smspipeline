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

    var that = this;

    this.doMassAction = function (element) {
        pressed_button = jQuery(element);

        if (pressed_button.hasClass('disabled')) {
            return false;
        }

        that.setupActiveButton(pressed_button);
        that.blockToolbarButtons();

        jQuery('#recordset_action').val(element.id);
        jQuery('#recordset').submit();
    };

    this.massActionError = function(xhr, ajaxOptions, thrownError) {
        that.restoreActiveButton();
        that.releaseToolbarButtons();

        message = jQuery('#success_message');
        that.resetMessage(message);
        message.addClass('error');
        jQuery('#success_message_body').html('fault');
        message.show();
    };

    this.massActionSuccess = function(json) {
        that.restoreActiveButton();
        that.releaseToolbarButtons();

        message = jQuery('#success_message');
        that.resetMessage(message);
        message.addClass('success');
        jQuery('#success_message_body').html('success');
        message.show();

        that.reload();
    };

    this.resetMessage = function(message) {
        message.removeClass('success');
        message.removeClass('error');
        message.removeClass('info');
    }

    this.setupActiveButton = function(pressed_button) {
        pressed_button.addClass('toolbar_ajax_blocker');
        pressed_button.html('Sending...');
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

    this.reload = function() {
        jQuery("#records_list").load(url_load_grid + '?ajax=1');
    };

    this.updateCheckbox = function(checkbox) {
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
    };

    this.updateAllCheckboxes = function(checkbox) {
        $('.list_item').attr('checked', checkbox.checked);
        if (checkbox.checked) {
            $('.massaction').removeClass('disabled');
        } else {
            $('.massaction').addClass('disabled');
        }
    }

};

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

function submitGridMassAction(e){
    e.preventDefault();
    var form = jQuery(e.target);
    jQuery.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: form.serialize(),
        dataType: 'json',
        success: Grid.massActionSuccess,
        error: Grid.massActionError
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
