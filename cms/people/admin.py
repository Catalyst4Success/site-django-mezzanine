from __future__ import unicode_literals

from django.contrib import admin
from copy import deepcopy

from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin, BaseDynamicInlineAdmin, DisplayableAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Person, PeoplePage, MemberCategory
# Register your models here.

class PeopleInline(StackedDynamicInlineAdmin):
    model = Person
    filter_horizontal = ("section",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("sections",)

    def __init__(self, *args, **kwargs):
       super(PeopleInline, self).__init__(*args, **kwargs) 
       fields = self.fields
       fields.append('section')

class MemberCategoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        return False;

class PeopleAdmin(PageAdmin):
    inlines = (PeopleInline,)

admin.site.register(PeoplePage, PeopleAdmin)
admin.site.register(MemberCategory, MemberCategoryAdmin)
