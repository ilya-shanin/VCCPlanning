from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(label = "Электронная почта",
                            widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label = "Пароль",
                            widget = forms.PasswordInput(attrs={"class": "form-control"}))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {"email": forms.EmailInput(attrs={"class": "form-control"}),
                   "first_name": forms.TextInput(attrs={"class": "form-control"}),
                   "last_name": forms.TextInput(attrs={"class": "form-control"})}

    password1 = forms.CharField(
            label="Пароль",
            widget=forms.PasswordInput(attrs={"class": "form-control"}),
            validators=[validate_password])
    password2 = forms.CharField(
            label="Подтвердите пароль",
            widget=forms.PasswordInput(attrs={"class": "form-control"}),
            validators=[validate_password])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'image', 'job', 'phonenumber', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]