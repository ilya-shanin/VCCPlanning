from django.shortcuts import render
from django.views.generic import View
from events.models import Conference
from participants.models import Participant
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

class EventDetailView(LoginRequiredMixin, View):
    login_url =     'accounts:signin'
    template_name = 'event_detail.html'

    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['pk']
        participants = Participant.objects.get_event_participants(event_id)
        try:
            conf_data = Conference.objects.get(pk=event_id)
        except Conference.DoesNotExist:
            raise Http404('Ничего не найдено')
        context = {
            'conf': conf_data,
            'part': participants
        }
        return render(request, self.template_name, context)