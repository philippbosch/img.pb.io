import os.path

from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from imagehost.conf import settings as imagehost_settings
from imagehost.models import Image

def show_image(request, slug):
    image_path = os.path.join(imagehost_settings.UPLOAD_DIR_PATH, "%s.png" % slug)
    if not os.path.exists(image_path):
        raise Http404, u"%s" % _("The requested image does not exist")
    image, created = Image.objects.get_or_create(slug=slug)
    # if created:
    image.file = image_path.replace(os.path.join(settings.MEDIA_ROOT,''), '')
    image.save()
    context = {
        'image': image,
    }
    return render_to_response('imagehost/image.html', context, context_instance=RequestContext(request))
