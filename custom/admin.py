from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.models import RichTextPage

from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, SingletonAdmin, StackedDynamicInlineAdmin

from .models import CatalystPage, HomePage, Section, GridPage, GridSection


class SectionInline(StackedDynamicInlineAdmin):
    model = Section

class CatalystPageAdmin(PageAdmin):
    inlines = (SectionInline,)

class GridSectionInline(StackedDynamicInlineAdmin):
    model = GridSection

class GridPageAdmin(PageAdmin):
    inlines = (GridSectionInline,)

class HomePageAdmin(PageAdmin):
    filter_horizontal = ("blog_posts",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("blog_posts",)

# Register your models here.
admin.site.unregister(RichTextPage)
admin.site.register(CatalystPage, CatalystPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(GridPage, GridPageAdmin)
