from django.urls import path, re_path
from events.views.events_view import ajax_response

from events.views import Events, SearchEventsView, EventDetailView, CalendarView

app_name = 'events'

urlpatterns = [
                path('', Events.as_view(), name='events-list'),
                path('search', SearchEventsView.as_view(), name='events-search')]
urlpatterns += [path('details/<int:pk>/', EventDetailView.as_view(), name='event-detail'),]
urlpatterns += [path('calendar/', CalendarView.as_view(), name='event-calendar'),]
urlpatterns += [path('calendar/ajax/load_events/', ajax_response, name='ajax-load'),]