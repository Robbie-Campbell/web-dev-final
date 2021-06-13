$(window).on('resize', function() {
    if($(window).width() < 800) {
        $('.recipe').addClass('d-block');
        $('.recipe').removeClass('d-flex');
    }else{
        $('.recipe').addClass('d-flex');
        $('.recipe').removeClass('d-block');
    }

});

$(window).on('load', function() {
    if($(window).width() < 800) {
        $('.recipe').addClass('d-block');
        $('.recipe').removeClass('d-flex');
    }else{
        $('.recipe').addClass('d-flex');
        $('.recipe').removeClass('d-block');
    }
});