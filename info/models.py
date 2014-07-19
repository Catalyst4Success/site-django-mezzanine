from django.db import models
from mezzanine.core.models import SiteRelated
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to

class SitewideContent(SiteRelated):
    email = models.CharField(_("Email"), max_length=100)
    phonenumber = models.CharField(_("Phone Number"), max_length=100)
    logo = FileField(_("Logo"), max_length=200, format="Image",
            upload_to=upload_to("Logo.file", "Logo File"))

    class Meta:
        verbose_name = _('Sitewide Content')
        verbose_name_plural = _('Sitewide Content')


# Create your models here.
