from __future__ import unicode_literals

from django.contrib import admin
from copy import deepcopy
from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin, BaseDynamicInlineAdmin, DisplayableAdmin
from mezzanine.pages.admin import PageAdmin
from .models import LocalChapter, LocalChaptersPage, Section, ChapterMember, ChapterPage, ChapterPicture, ChapterPictureCategory
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

class SectionInline(StackedDynamicInlineAdmin):
    model = Section
"""
class ChapterPictureCategoryFilter(SimpleListFilter):
    title = _('picture_category')
    parameter_name = _('picture_category')

    def lookups(self, request, model_admin):
        chapterCategories = set([c.picture_category for c in model_admin.model.objects.all()])
        return [(c.id, c.page) for c in chapterCategories]

    def queryset(self, request,queryset):
        if self__page.value():
            return queryset.filter(picture_category__page__id__exact = self.page.value())
        else:
            return queryset
            """

class ChapterPictureInline(TabularDynamicInlineAdmin):
    model = ChapterPicture
    filter_horizontal = ("picture_category",)
    list_filter = ("picture_category",)

    def __init__(self, *args, **kwargs):
        super(ChapterPictureInline, self).__init__(*args, **kwargs)
        fields = self.fields  
        fields.append("picture_category")



"""
class ChapterMembersInline(StackedDynamicInlineAdmin):
    model = Person

    def __init__(self, *args, **kwargs):
       super(PeopleInline, self).__init__(*args, **kwargs) 
       fields = self.fields

class ChapterMembersAdmin(PageAdmin):
    inlines = (ChapterMembersInline,)

    def __init__(self, *args, **kwargs):
        super(ChapterMembersAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])
"""

class ChapterPictureCategoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title", "page",)}),)

    def in_menu(self):
        return True;

class ChapterPictureAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("file","picture_category",)}),)


class ChapterMemberAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("name","position","email", "file", "bio")}),)

    def in_menu(self):
        return True;

class LocalChaptersPageAdmin(PageAdmin):

    filter_horizontal = ("chapters",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("chapters",)
    inlines = (SectionInline,)

    def __init__(self, *args, **kwargs):

        super(LocalChaptersPageAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

class ChapterPageAdmin(PageAdmin):

    inlines = (ChapterPictureInline,)

    def __init__(self, *args, **kwargs):
        super(ChapterPageAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets


class LocalChapterAdmin(admin.ModelAdmin):

    fieldsets = ((None, {"fields": ("schoolName","schoolAddress","schoolCity", "schoolState", "schoolZipCode", "page","members","chapterNumber","chapterEmail")}),)
    filter_horizontal = ("members",)

    def in_menu(self):
        return True;


admin.site.register(ChapterPage, ChapterPageAdmin)
admin.site.register(LocalChaptersPage, LocalChaptersPageAdmin)
admin.site.register(LocalChapter, LocalChapterAdmin)
admin.site.register(ChapterMember, ChapterMemberAdmin)
admin.site.register(ChapterPictureCategory, ChapterPictureCategoryAdmin)


# Register your models here.

