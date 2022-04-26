from django.shortcuts import render
from django.views.generic import View
from events.models import Conference
from participants.models import Participant

# Create your views here.

class Events(View):
    template_name = 'events_list.html'
    confs = Conference.objects.all()
    confs_count = confs.count()
    participants = Participant.objects.all()
    part_count = participants.count()

    def get(self, request):
        context = {'conferences': self.confs,
                   'confs_count': self.confs_count,
                   'participants': self.participants,
                   'part_counts': self.part_count}
        return render(request, self.template_name, context)