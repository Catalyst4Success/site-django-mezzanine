from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText

class CatalystPage(Page, RichText):
    title_color = models.CharField(_("Title Color"), max_length=10, blank=True) 
    navbar_title = models.CharField(_("Title on Navbar"), max_length=20, blank=True) 
    font_awesome_icon = models.CharField(_("Font Awesome Icon"), max_length=20, blank=True)
    class Meta:
        verbose_name = _("Catalyst Page")
        verbose_name_plural = _("Catalyst Pages")

# Create your models here.
