from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import PeoplePage

@processor_for(PeoplePage)
def people_extra(request, page):
    nolabel = page.peoplepage.people.filter(member_category=None)
    return {"nolabel": nolabel}
