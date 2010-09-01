$(document).ready(function() {
    var zoomLink = $('a.zoom');
    zoomLink.click(function(e) {
        e.preventDefault();
        var $img = $('.image img');
        if (!$img.data('originalLoaded')) {
            $img.attr('src', $img.attr('longdesc'));
            $img.data('originalLoaded', true);
            $img.bind('load', function() {
            });
        }
        $img.parents('.image').toggleClass('small large');
        $(this).toggleClass('in out');
    });
    $('.edit, .delete').click(function(e) {
        e.preventDefault();
        var win = window.open($(this).attr('href') + '?_popup=1', 'img_edit_delete', 'height=500,width=800,resizable=yes,scrollbars=yes');
        win.focus();
        return false;
    });
    $('.links').append('<div class="title"></div>');
    $('.links a').hover(function() {
        $(this).parents('.links').find('.title').text($(this).find('span').text());
    }, function() {
        if ($(this).parents('.links').find('.title').text() == $(this).find('span').text()) {
            $(this).parents('.links').find('.title').text('');
        }
    });
    
    ZeroClipboard.setMoviePath(settings.MEDIA_URL + 'js/lib/zeroclipboard/ZeroClipboard10.swf');
    var clip = new ZeroClipboard.Client();
    clip.setText($('.links a.copy').attr('href'));
    clip.glue($('.links a.copy').get(0));
    clip.addEventListener('onMouseOver', function() {
        $('.image').addClass('hover');
        $('a.copy').trigger('mouseover');
    });
    clip.addEventListener('onMouseOut', function() {
        $('.image').removeClass('hover');
        $('a.copy').trigger('mouseout');
    });
    clip.addEventListener('onComplete', function() {
        $('.links .title').text('URL copied to clipboard!');
    });
});