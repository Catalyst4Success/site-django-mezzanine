from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.models import RichTextPage

from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, SingletonAdmin

from .models import CatalystPage, HomePage

class CatalystPageAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)
class HomePageAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)

# Register your models here.
admin.site.unregister(Form)
admin.site.unregister(RichTextPage)
admin.site.register(CatalystPage, CatalystPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
