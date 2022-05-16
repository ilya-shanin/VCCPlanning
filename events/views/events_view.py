from django.shortcuts import render
from django.views.generic import ListView
from events.models import Conference
from participants.models import Participant
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.core import serializers

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

def ajax_response(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            events = []
            running_confs = Participant.objects.get_today_events(user=request.user)
            for conf in running_confs:
                events += Conference.objects.filter(id=conf.event_id).values()
            #day = request.GET.get('date')
            #running_confs = Participant.objects.get_day_events(user=request.user, day)
            print(events)
            return JsonResponse({'context': events})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')