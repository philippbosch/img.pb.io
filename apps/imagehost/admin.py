from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from imagehost.models import Image

from easy_thumbnails.files import get_thumbnailer

class ImageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'thumbnail_tag', 'title', 'created_on',)
    list_display_links = ('slug', 'title',)
    
    def thumbnail_tag(self, instance):
        if not instance.file:
            return ""
        opts = {
            'size': (160,160),
        }
        return u'<img src="%s">' % get_thumbnailer(instance.file).get_thumbnail(opts).url
    thumbnail_tag.allow_tags = True
    thumbnail_tag.short_description = _("preview")

admin.site.register(Image, ImageAdmin)
