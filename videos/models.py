from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Orderable, RichText

# Create your models here.

class VideosPage(Page, RichText):

    class Meta:
        verbose_name = _("Videos Page")
        verbose_name_plural = _("Videos Pages")

class Video(Orderable):
    name = models.CharField(_("Video Name"), max_length=1000)
    link = models.CharField(_("Video Link"), max_length=1000)
    videosPage = models.ForeignKey("VideosPage", related_name="videos")

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
