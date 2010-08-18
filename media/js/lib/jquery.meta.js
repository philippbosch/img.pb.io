(function($) {
    $.fn.meta = function(m) {
        var c = $(this).attr('class');
        if (!c) return false;
        var classes = c.split(" ");
        meta = [];
        for (var i=0; i<classes.length; i++) {
            if (classes[i].substring(0,m.length) == m) meta[meta.length] = classes[i].substring(m.length+1,classes[i].length);
        }
        return meta;
    };
})(jQuery);
