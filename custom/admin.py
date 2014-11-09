from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.pages.models import RichTextPage, Link

from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, SingletonAdmin, StackedDynamicInlineAdmin, TabularDynamicInlineAdmin

from .models import CatalystPage, HomePage, Section, GridPage, GridSection

class SectionInline(StackedDynamicInlineAdmin):
    model = Section

class CatalystPageAdmin(PageAdmin):
    inlines = (SectionInline,)
    def __init__(self, *args, **kwargs):
        super(CatalystPageAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

class GridSectionInline(StackedDynamicInlineAdmin):
    model = GridSection

class GridPageAdmin(PageAdmin):
    inlines = (GridSectionInline,)
    def __init__(self, *args, **kwargs):
        super(GridPageAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

class HomePageAdmin(PageAdmin):
    filter_horizontal = ("blog_posts",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("blog_posts",)

    def __init__(self, *args, **kwargs):
        super(HomePageAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

class GalleryImageInline(TabularDynamicInlineAdmin):
    model = GalleryImage

class GalleryAdmin(PageAdmin):
    inlines = (GalleryImageInline,)

    class Media:
        css = {"all": ("mezzanine/css/admin/gallery.css",)}

    def __init__(self, *args, **kwargs):
        super(GalleryAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])


class LinkAdmin(PageAdmin):

    def __init__(self, *args, **kwargs):
        super(LinkAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets[:1]
        fieldsets[0][1]["fields"].pop(1)
        fieldsets[0][1]["fields"].pop(1)
        fieldsets[0][1]["fields"] = fieldsets[0][1]["fields"][:-1]
        fieldsets[0][1]["fields"].insert(1, ["font_awesome_icon","navbar_title","title_color",])
        fieldsets[0][1]["fields"].extend(["slug",])


    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Make slug mandatory.
        """
        if db_field.name == "slug":
            kwargs["required"] = True
        return super(LinkAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def save_form(self, request, form, change):
        """
        Don't show links in the sitemap.
        """
        obj = form.save(commit=False)
        if not obj.id and "in_sitemap" not in form.fields:
            obj.in_sitemap = False
        return super(LinkAdmin, self).save_form(request, form, change)


# Register your models here.
admin.site.unregister(RichTextPage)
admin.site.unregister(Gallery)
admin.site.unregister(Link)
admin.site.register(Link, LinkAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(CatalystPage, CatalystPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(GridPage, GridPageAdmin)
