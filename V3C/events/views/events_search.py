from django.shortcuts import render
from django.views.generic import ListView
from events.models import Conference

class SearchEventsView(ListView):
    model = Conference
    template_name = 'search_results.html'
    paginate_by = 7
    context_object_name = 'conferences'

    def get_context_data(self, **kwargs):
        context = super(SearchEventsView, self).get_context_data(**kwargs) 
        context['confs_count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.filter(name__icontains=self.request.GET.get('q'))
