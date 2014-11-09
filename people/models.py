from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Orderable, RichText, Slugged
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.utils.models import upload_to
from mezzanine.generic.fields import KeywordsField


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
    member_category = models.ManyToManyField("MemberCategory", verbose_name=_("Member Category"), blank=True, related_name="people") 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")


class MemberCategory(Slugged):
    page = models.ForeignKey("PeoplePage", related_name="categories") 
    heading_bar_color = models.CharField(_("Heading Bar Color"), max_length=10, blank=True)
    rank = models.PositiveIntegerField()
    class Meta:
        verbose_name = _("Member Category")
        verbose_name_plural = _("Member Categories")
        ordering = ("title",)


# Create your models here.
