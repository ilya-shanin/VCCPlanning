from ast import Delete
from django.views.generic import View, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy

from accounts.models import User
from accounts.forms import ProfileEditForm, DeleteUserForm

class ProfileView(LoginRequiredMixin, View):
    login_url = 'accounts:signin'
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        try:
            user_data = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            raise Http404('Пользователь не найден')

        context = {
            'user_data': user_data
        }
        return render(request, self.template_name, context)

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    succes_url = 'accounts:profile'
    template_name = 'edit_profile.html'

    def get_object(self, queryset=None): 
        return get_object_or_404(User, id=self.request.user.id)

    def form_valid(self, form):
        #save cleaned post data
        clean = form.cleaned_data 
        context = {}        
        self.object = context.update(clean) 
        return super(EditProfileView, self).form_valid(form)
    
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    success_message = 'Пароль успешно изменен'
    template_name = 'change_password.html'
    success_url = reverse_lazy('accounts:profile')

class DeleteProfileView(DeleteView):
    template_name = 'profile_delete.html'
    form_class = DeleteUserForm
    success_url = reverse_lazy('accounts:signin')

    def get_object(self, queryset=None): 
        return get_object_or_404(User, id=self.request.user.id)

    def form_valid(self, form):
        #delete validation with password
        clean = form.cleaned_data
        current_password = self.request.user.password 
        if check_password(clean['password'] , current_password):
            return super(DeleteProfileView, self).form_valid(form)
        else:
            form.add_error('password', 'Неверный пароль')
            return render(self.request, self.template_name, {"form": form})

