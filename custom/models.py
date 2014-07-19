from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText, Orderable
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.blog.models import BlogPost
from mezzanine.utils.models import upload_to

class CatalystPage(Page, RichText):
    class Meta:
        verbose_name = _("Section Page")
        verbose_name_plural = _("Section Pages")

class Section(Orderable):
    page = models.ForeignKey("CatalystPage", related_name="sections")
    title = models.CharField(_("Section Title"), max_length=100)
    heading_bar_color = models.CharField(_("Heading Bar Color"), max_length=10, blank=True)
    textfield = RichTextField(_("Content"), blank=True)

    def __str__(self):
        return self.title

class GridPage(Page, RichText):
    class Meta:
        verbose_name = _("Grid Page")
        verbose_name_plural = _("Grid Pages")

class GridSection(Orderable):
    page = models.ForeignKey("GridPage", related_name="gridsection")
    title = models.CharField(_("Section Title"), max_length = 100)
    icon = models.CharField(_("Section Icon"), max_length = 100)
    textfield = RichTextField(_("Content"), blank=True)

class HomePage(Page, RichText):
    text1 = models.CharField(_("Title sub-text"), max_length = 100, blank=True)

    quoteA = models.TextField(_("Section 1 (Quote)"), blank=True)
    quoteAttr = models.CharField(_("Quote Attribute"), max_length = 100, blank=True)
    quoteColor = models.CharField(_("Section 1 Background Color"), max_length = 100, blank=True)

    section2Title = models.CharField(_("Section 2 Title(Latest News)"), max_length = 100, blank=True)
    section2SubTitle = models.CharField(_("Section 2 Sub Title"), max_length = 100, blank=True)
    section2Color = models.CharField(_("Section 2 Background Color"), max_length = 100, blank=True)
    section2ButtonTitle = models.CharField(_("Button Title"), max_length = 100, blank=True)
    blog_posts = models.ManyToManyField("blog.BlogPost", verbose_name=_("Press Releases"), blank=True, related_name="pressreleases") 

    section3BackgroundPicture = FileField(_("File"), max_length=200, format="Image",
            upload_to=upload_to("Homepage.file", "HomePage"))

    section3ButtonTitle = models.CharField(_("Button Title"), max_length = 100, blank=True)
    section3Link = models.CharField(_("Button Link"), max_length = 100, blank=True)


    section4Title = models.CharField(_("Section 2 Title(Fact of the Day)"), max_length = 100, blank=True)
    section4BackgroundColor = models.CharField(_("Section 2 Background Color"), max_length = 100, blank=True)


    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

# Create your models here.
