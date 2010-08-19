from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<slug>[^/]+)$', 'imagehost.views.show_image', name='imagehost_show_image'),
    url(r'^(?P<slug>[^/]+)/download/$', 'imagehost.views.download_image', name='imagehost_download_image'),
)
