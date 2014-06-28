from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Orderable, RichText, Slugged
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.utils.models import upload_to
from mezzanine.generic.fields import KeywordsField
from custom.models import CatalystPage

class LocalChaptersPage(Page, RichText):
    chapters = models.ManyToManyField("LocalChapter", verbose_name=_("Local Chapters"), blank=True, related_name="chapters")
    file = FileField(_("File"), max_length=200, format="Image",
            upload_to=upload_to("LocalChapters.file", "Map File"))
    extra_info = RichTextField(_("Lower Text"), blank=True)
        
    class Meta:
        verbose_name = _("Local Chapters Page")
        verbose_name_plural = _("Local Chapters Pages")

class Section(Orderable):
    page = models.ForeignKey("LocalChaptersPage", related_name="sections")
    title = models.CharField(_("Section Title"), max_length=100)
    
    heading_bar_color = models.CharField(_("Heading Bar Color"), max_length=10, blank=True)
    textfield = RichTextField(_("Content"), blank=True)

    def __str__(self):
        return self.title


class LocalChapter(Orderable):

    schoolName = models.CharField(_("School Name"), max_length=100)
    schoolAddress = models.CharField(_("School Address"), max_length=100)
    schoolCity = models.CharField(_("School City"), max_length=100)
    schoolState = models.CharField(_("School State"), max_length=100)
    schoolZipCode = models.CharField(_("School Zip Code"), max_length=100)
    chapterWebsite = models.CharField(_("Chapter Website"), max_length=100, blank=True)
    chapterNumber = models.CharField(_("Chapter Phone Number"), max_length=100, blank=True)
    chapterEmail = models.CharField(_("Chapter Email Address"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Local Chapter")
        verbose_name_plural = _("Local Chapters")

    def __str__(self):
        return self.schoolName


# Create your models here.
