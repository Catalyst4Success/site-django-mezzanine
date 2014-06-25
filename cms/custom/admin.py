from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.models import RichTextPage

from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, SingletonAdmin, StackedDynamicInlineAdmin

from .models import CatalystPage, HomePage, Section

class SectionInline(StackedDynamicInlineAdmin):
    model = Section

class CatalystPageAdmin(PageAdmin):
    inlines = (SectionInline,)


# Register your models here.
admin.site.unregister(Form)
admin.site.unregister(RichTextPage)
admin.site.register(CatalystPage, CatalystPageAdmin)
admin.site.register(HomePage, PageAdmin)
