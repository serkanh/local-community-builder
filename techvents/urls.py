from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from techvents import views

urlpatterns = patterns('',
    url(r'^events/$', TemplateView.as_view(template_name='techvents/event_index.html'), name='event-home'),
    url(r'^events/type/([^/]+)/$', views.event_type, name='tech-event'),
    (r'^swingtime/', include('swingtime.urls')),
)
