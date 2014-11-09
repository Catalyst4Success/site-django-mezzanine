from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Orderable, RichText, Slugged
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.utils.models import upload_to
from mezzanine.generic.fields import KeywordsField
from project.custom.models import CatalystPage
from django.db.models import F



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
    page = models.ForeignKey("ChapterPage", related_name="Page", blank=True, null=True)
    chapterNumber = models.CharField(_("Chapter Phone Number"), max_length=100, blank=True)
    chapterEmail = models.CharField(_("Chapter Email Address"), max_length=100, blank=True)
    members = models.ManyToManyField("ChapterMember", verbose_name=_("Chapter Members"), blank=True, related_name="members")

    class Meta:
        verbose_name = _("Local Chapter")
        verbose_name_plural = _("Local Chapters")

    def __str__(self):
        return self.schoolName

class ChapterPage(Page, RichText):

    firstBackgroundPicture = FileField(_("File"), max_length=200, format="Image", null=True,
            upload_to=upload_to("ChapterPage.file", "ChapterPage"))
    
    aboutHeader = models.CharField(_("About header"), max_length = 100)
    aboutText = models.TextField(_("About text"))

    eventsHeader = models.CharField(_("Events header"), max_length = 100)
    eventsText = models.TextField(_("Events text"))
    
    handsonHeader = models.CharField(_("Hands-on header"), max_length = 100)
    handsonText = models.TextField(_("Hands-on text"))
    secondBackgroundPicture = FileField(_("File"), max_length=200, format="Image", null=True,
            upload_to=upload_to("ChapterPage.file", "ChapterPage"))

    showsHeader = models.CharField(_("Shows header"), max_length = 100)
    showsText = models.TextField(_("Shows text"))
    thirdBackgroundPicture = FileField(_("File"), max_length=200, format="Image", null=True,
            upload_to=upload_to("ChapterPage.file", "ChapterPage"))

    
    contactHeader = models.CharField(_("Contact header"), max_length = 100)
    contactText = models.TextField(_("Contact text"))
    chapter = models.ForeignKey("LocalChapter", related_name="Chapter")
    
    class Meta:
        verbose_name = _("Chapter Page")
        verbose_name_plural = _("Chapter Pages")


class ChapterPictureCategory(Slugged):
    page = models.ForeignKey("ChapterPage", related_name="ChapterPictureCategories", null=True)
    class Meta:
        verbose_name = _("Chapter Picture Category")
        verbose_name_plural = _("Chapter Picture Categories")


class ChapterPicture(Orderable):
    page = models.ForeignKey("ChapterPage", related_name="ChapterPictures")
    picture_category = models.ManyToManyField("ChapterPictureCategory", verbose_name=_("Chapter Picture Category"), blank=True, related_name="picture", limit_choices_to = {'page': F('page')}) 
    file = FileField(_("File"), max_length=200, format="Image",
                     upload_to=upload_to("Localchapters.ChapterPicture.file", "Localchapters"))
    class Meta:
        verbose_name = _("Chapter Picture")
        verbose_name_plural = _("Chapter Pictures")



class ChapterMember(Orderable):
    name = models.CharField(_("Name"), max_length = 100)
    position = models.CharField(_("Position/Description"), max_length = 100, blank=True)
    email = models.CharField(_("Email Address"), max_length = 200, blank=True)
    file = FileField(_("File"), max_length=200, format="Image",
                     upload_to=upload_to("Localchapters.ChapterMember.file", "Localchapters"))
    bio = RichTextField(_("Bio"), blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Chapter Member")
        verbose_name_plural = _("Chapter Members")

# Create your models here.
