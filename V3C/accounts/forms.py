from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.files.images import get_image_dimensions
from django.urls import reverse_lazy
from PIL import Image

from accounts.models import User


class SignInForm(forms.Form):
    email =     forms.EmailField(
                                label = 'Электронная почта',
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password =  forms.CharField(
                                label = 'Пароль',
                                widget = forms.PasswordInput(attrs={'class': 'form-control'}))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'})}

    password1 = forms.CharField(
                                label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                validators=[validate_password])
    password2 = forms.CharField(
                                label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                validators=[validate_password])

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'image', 'job', 'phonenumber', 'is_active', 'is_superuser')

    def clean_password(self):

        return self.initial['password']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'job', 'phonenumber']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'image': forms.FileInput(attrs={'class': 'form-control-file'}),
                    'job': forms.TextInput(attrs={'class': 'form-control'}),
                    'phonenumber': forms.TextInput(attrs={'class': 'form-control phone-field', 'placeholder': '+7(000)000-00-00'})}

    def clean_image(self):
        image = self.cleaned_data['image']
        try:
            #validate dimensions
            max_width = max_height = 400
            if image.width > max_width or image.height > max_height:
                img = Image.open(image)
                size = (max_width, max_height)
                image = img.thumbnail(size)

            #validate content type
            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'png']):
                raise forms.ValidationError('Пожайлуйста используйте файл формата jpeg или png')

            #validate file size
            if image._size > (2 * 1024 * 1024):
                raise forms.ValidationError('Размер картинки не должен превышать 2мБ')

        except AttributeError:
            pass

        return image

class DeleteUserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['password']
    
    password = forms.CharField(
                            label = "Пароль",
                            widget = forms.PasswordInput(attrs={"class": "form-control"}))