function request(validate_url, is_email, str, icon) {
    $.ajax({
        url: validate_url,
        data:{
            isEmail: is_email,
            value: str
        },
        dataType: 'json',
        success: function (data) {
            if(data['available']){
                icon.css('visibility', 'visible');
            } else {
                icon.css('visibility', 'hidden');
            }

        }
    });
}

function validate_user() {
    let username_input = $('#id_username')
    let url = username_input.attr('data-validate-url')
    request(url, false, username_input.val(), $('#i_username'));
    username_input.change(function () {
        request(url, false, $(this).val(), $('#i_username'));
    });
}

function validate_email() {
    let email_input = $('#id_email')
    let url = email_input.attr('data-validate-url')
    request(url, true, email_input.val(), $('#i_email'));
    email_input.change(function () {
        request(url, true, $(this).val(), $('#i_email'));
    });
}