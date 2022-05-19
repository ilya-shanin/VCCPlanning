from django.urls import path, re_path

from events.views import Events, SearchEventsView, EventDetailView

app_name = 'events'

urlpatterns = [
                path('', Events.as_view(), name='events-list'),
                path('search', SearchEventsView.as_view(), name='events-search')]
urlpatterns += [path('details/<int:pk>/', EventDetailView.as_view(), name='event-detail'),]
