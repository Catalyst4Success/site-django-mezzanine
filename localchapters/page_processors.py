from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import ChapterPage 
"""
@processor_for(ChapterPage)
def chapter_extra(request, page):
    nolabel = page.peoplepage.people.filter(member_category=None)
    rankorder = page.peoplepage.categories.order_by('rank')

    return {"nolabel": nolabel, "rankorder": rankorder}
    """
