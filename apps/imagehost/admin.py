from django.contrib import admin

from imagehost.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'created_on',)

admin.site.register(Image, ImageAdmin)
