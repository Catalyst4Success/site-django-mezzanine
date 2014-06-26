from __future__ import unicode_literals

from django.contrib import admin
from copy import deepcopy
from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin, BaseDynamicInlineAdmin, DisplayableAdmin
from mezzanine.pages.admin import PageAdmin
from .models import LocalChapter, LocalChaptersPage, Section

class SectionInline(StackedDynamicInlineAdmin):
    model = Section

class LocalChaptersPageAdmin(PageAdmin):
    filter_horizontal = ("chapters",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("chapters",)
    inlines = (SectionInline,)


class LocalChapterAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("schoolName","schoolAddress","schoolCity", "schoolState", "schoolZipCode", "chapterWebsite","chapterNumber","chapterEmail")}),)

    def in_menu(self):
        return True;

admin.site.register(LocalChaptersPage, LocalChaptersPageAdmin)
admin.site.register(LocalChapter, LocalChapterAdmin)


# Register your models here.

