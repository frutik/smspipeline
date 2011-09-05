function do_submit() {
    jQuery("#add_form").submit();
}

function do_cancel() {
    hide_create_window();
}

function hide_create_window() {
    jQuery('#create_form').hide();
}

function enable_window_buttons() {
    jQuery("#save_button").removeClass('disabled');
    jQuery("#cancel_button").removeClass('disabled');
}

function disable_window_buttons() {
    jQuery("#save_button").addClass('disabled');
    jQuery("#cancel_button").addClass('disabled');
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
