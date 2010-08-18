$(document).ready(function() {
    var zoomLink = $('<a href="#"></a>');
    zoomLink.click(function() {
        var $img = $(this).find('img');
        $img.css({
            'width': $img.width() + 'px',
            'height': $img.height() + 'px'
        });
        $img.attr('src', $img.data('original'));
        $img.bind('load', function() {
            $(this).animate({
                'width': $(this).meta('width')[0] + 'px', 
                'height': $(this).meta('height')[0] + 'px'
            }, {
                'duration': 500
            });
        });
    });
    $('#image').data({
        'small': $('#image').attr('src'),
        'original': $('#image').attr('longdesc')
    }).wrap(zoomLink);
});