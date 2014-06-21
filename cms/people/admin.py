from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Person, PeoplePage 
# Register your models here.

class PeopleInline(TabularDynamicInlineAdmin):
    model = Person

class PeopleAdmin(PageAdmin):
    inlines = (PeopleInline,)

admin.site.register(PeoplePage, PeopleAdmin)
