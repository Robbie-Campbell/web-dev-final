$(window).on('resize', function() {
    if($(window).width() < 700) {
        $('#recipe').addClass('d-block');
        $('#recipe').removeClass('d-flex');
    }else{
        $('#recipe').addClass('d-flex');
        $('#recipe').removeClass('d-block');
    }
});