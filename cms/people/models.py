from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Orderable, RichText
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.utils.models import upload_to

class PeoplePage(Page, RichText):
        
    class Meta:
        verbose_name = _("People Page")
        verbose_name_plural = _("People Pages")

class Person(Orderable):
    page = models.ForeignKey("PeoplePage", related_name="people") 
    name = models.CharField(_("Name"), max_length = 100)
    position = models.CharField(_("Position/Description"), max_length = 100, blank=True)
    email = models.CharField(_("Email Address"), max_length = 200, blank=True)
    file = FileField(_("File"), max_length=200, format="Image",
            upload_to=upload_to("People.Person.file", "People"))
    bio = RichTextField(_("Bio"), blank=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")


# Create your models here.
