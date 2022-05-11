from django.shortcuts import render
from django.views.generic import ListView
from events.models import Conference
from participants.models import Participant

# Create your views here.

class Events(ListView):
    model = Conference
    template_name = 'events_list.html'
    paginate_by = 7
    context_object_name = 'conferences'

    confs = Conference.objects.all()
    confs_count = confs.count() 

    def get_context_data(self, **kwargs):
        context = super(Events, self).get_context_data(**kwargs) # get the default context data
        context['confs_count'] = self.confs_count # add extra field to the context
        return context