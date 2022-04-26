from django.urls import path

from events.views.events_view import Events

app_name = "events"

urlpatterns = [
    path("", Events.as_view(), name="events-list"),
]