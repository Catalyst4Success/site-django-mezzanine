from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText, Orderable
from mezzanine.core.fields import RichTextField

class CatalystPage(Page, RichText):
    class Meta:
        verbose_name = _("Catalyst Page")
        verbose_name_plural = _("Catalyst Pages")

class Section(Orderable):
    page = models.ForeignKey("CatalystPage", related_name="sections")
    title = models.CharField(_("Section Title"), max_length=100)
    heading_bar_color = models.CharField(_("Heading Bar Color"), max_length=10, blank=True)
    textfield = RichTextField(_("Content"), blank=True)

    def __str__(self):
        return self.title

class HomePage(Page):
    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")



# Create your models here.
