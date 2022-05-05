from django.views.generic import View
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from accounts.forms import SignInForm


class SignInView(View):
    """ User registration view """

    template_name = "sign_in.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("dashboard") # REDIRECT HERE
        forms.add_error(None, 'Неправильное имя пользователя или пароль!')
        context = {"form": forms}
        return render(request, self.template_name, context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'reset/password_reset.html'
    email_template_name = 'reset/password_reset_email.html'
    subject_template_name = 'reset/password_reset_subject.txt'
    success_message = "Мы выслали на указанный вами электронный адрес инструкцию по сбросу пароля, " \
                      "если аккаунт с таким адрессом существует, вы скоро её получите." \
                      "Если письмо не пришло, " \
                      "пожалуйста убедитесь в правильности введенного электронного адреса и проверьте папку 'Спам'."
    success_url = reverse_lazy('accounts:email-sent')