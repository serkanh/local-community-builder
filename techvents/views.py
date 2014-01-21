# Create your views here.
from datetime import datetime, timedelta
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from swingtime import models as swingtime

#-------------------------------------------------------------------------------
def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    return render_to_response(
        'techvents/upcoming_by_event_type.html',
        dict(occurrences=occurrences, event_type=event_type),
        context_instance=RequestContext(request)
    )