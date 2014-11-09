from __future__ import unicode_literals

from django.contrib import admin
from copy import deepcopy

from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin, BaseDynamicInlineAdmin, DisplayableAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Person, PeoplePage, MemberCategory

# Register your models here.

class PeopleInline(StackedDynamicInlineAdmin):
    model = Person
    filter_horizontal = ("member_category",)
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("member_category",)

    def __init__(self, *args, **kwargs):
       super(PeopleInline, self).__init__(*args, **kwargs) 
       fields = self.fields
       fields.append('member_category')

class MemberCategoryAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ("title","page","heading_bar_color","rank",)}),)

    def in_menu(self):
        return True;

class PeopleAdmin(PageAdmin):
    inlines = (PeopleInline,)

    def __init__(self, *args, **kwargs):
        super(PeopleAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

admin.site.register(PeoplePage, PeopleAdmin)
admin.site.register(MemberCategory, MemberCategoryAdmin)
