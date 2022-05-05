from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from participants.models import Participant

class DashboardView(LoginRequiredMixin, View):
    login_url =     'accounts:signin'
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        confs = Participant.objects.get_all_user_events(user=request.user)
        running_confs = Participant.objects.get_running_events(user=request.user)
        context = {
            'total_count': confs.count(),
            'now_running': running_confs
        }
        return render(request, self.template_name, context)