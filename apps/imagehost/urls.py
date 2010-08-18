from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<slug>[^/]+)$', 'imagehost.views.show_image', name='imagehost_show_image'),
)
