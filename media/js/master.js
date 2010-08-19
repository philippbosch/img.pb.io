$(document).ready(function() {
    var zoomLink = $('<a href="#"></a>');
    zoomLink.click(function(e) {
        e.preventDefault();
        var $img = $(this).find('img');
        if (!$img.data('originalLoaded')) {
            $img.attr('src', $img.attr('longdesc'));
            $img.data('originalLoaded', true);
            $img.bind('load', function() {
            });
        }
        $img.parents('.image').toggleClass('small large');
    });
    $('.image.scalable img').wrap(zoomLink);
});