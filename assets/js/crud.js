function showCreateDialog(id) {
    $('.alert-message').hide();
    $('#modal_body').load(url_record_add);
    $(id).show();
}
