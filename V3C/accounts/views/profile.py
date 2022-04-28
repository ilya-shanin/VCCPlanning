from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from accounts.models import User

class ProfileView(LoginRequiredMixin, View):
    login_url = 'accounts:signin'
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        try:
            user_data = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise Http404('Пользователь не найден')

        context = {
            "user_data": user_data
        }
        return render(request, self.template_name, context)