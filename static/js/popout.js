jQuery(document).ready(function($) {
    //check for popup cookie if set don't open the dialog.

    // if (!Get_Cookie('popout')) {

    //console.log($('.popupDiv'));
    $(window).on("load", function() {
        // var width = $(window).width();
        // if(width >= 767){
        setTimeout(function() {
            // $('#main-pop').modal('show');
            // $('#float-btn').click();
            $('.form-title').html('Enquire Now');
            $('#enq-form .source').val('Float Form');
        }, 2000);
        // }
    });
    // }

    $('.modal .btn-close').click(function() {
        Set_Cookie('popout', 'it works', '', '/', '', '');
        // $('.popupDiv').fadeOut(1000);
        // $('.overlay').fadeOut(1000);
    });

    // $('.popupDiv .popupBg').click(function () {
    //     Set_Cookie('popout', 'it works', '', '/', '', '');
    //     $('.popupDiv').fadeOut(1000);
    //     $('.overlay').fadeOut(1000);
    // });

});