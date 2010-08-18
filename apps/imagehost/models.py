import os.path

from django.core.files.images import ImageFile
from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagehost.conf import settings as imagehost_settings

class Image(models.Model):
    slug = models.CharField(verbose_name=_("slug"), max_length=100, unique=True)
    file = models.ImageField(verbose_name=_("file"), upload_to=imagehost_settings.UPLOAD_DIR_PATH)
    title = models.CharField(verbose_name=_("title"), max_length=100, blank=True)
    created_on = models.DateTimeField(verbose_name=_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name=_("updated on"), auto_now=True, db_index=True)
    
    class Meta:
        verbose_name=_("image")
        verbose_name_plural=_("images")
        ordering = ('-created_on',)
    
    def __unicode__(self):
        return u"%s" % self.slug
    
    @models.permalink
    def get_absolute_url(self):
        return ('imagehost_show_image', (self.slug,))
    
    @property
    def original_url(self):
        return '%s%s.png' % (imagehost_settings.UPLOAD_DIR_URL, self.slug,)
    
    @property
    def original_path(self):
        return os.path.join(imagehost_settings.UPLOAD_DIR_PATH, '%s.png' % self.slug)
    
    @property
    def original_file(self):
        return open(self.original_path)
    
    @property
    def original_image(self):
        return ImageFile(self.original_file)