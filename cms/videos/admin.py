from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Video, VideosPage 
# Register your models here.

class VideosInline(TabularDynamicInlineAdmin):
    model = Video

class VideoAdmin(PageAdmin):
    inlines = (VideosInline,)

admin.site.register(VideosPage, VideoAdmin)
