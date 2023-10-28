$(document).ready(() => {
    // search by section
    $('.search-by-container').click(() => {
        $('.search-by-option').toggle();
        $('.search-by-button img').toggleClass('rotate');
        $('.search-by-button').toggleClass('radius');
    });

    $('input[name="search-by-option"]').change(function() {
        if ($(this).is(':checked')) {
          $('.search-by-button').html('Search By&nbsp;&nbsp;+1 <img src="../static/icons/chevron-down-reversed.svg" alt="chevron-down icon">');
          
        }
    });
    // search section
    $('.search-input').on('focus', () => {
        $('.search-input').addClass('input-color');
    });

    $('.search-input').on('blur', () => {
        $('.search-input').removeClass('input-color');
    });
});