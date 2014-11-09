from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin, DisplayableAdmin
from .models import Video, VideosPage 
from copy import deepcopy
# Register your models here.

class VideosInline(TabularDynamicInlineAdmin):
    model = Video

class VideoAdmin(PageAdmin):
    inlines = (VideosInline,)
    def __init__(self, *args, **kwargs):
        super(VideoAdmin, self).__init__(*args, **kwargs)
        fieldsets = self.fieldsets
        fieldsets[0][1]["fields"].insert(1,["font_awesome_icon","navbar_title","title_color",])

admin.site.register(VideosPage, VideoAdmin)
