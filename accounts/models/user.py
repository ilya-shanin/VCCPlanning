
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Custom User Manager

class UserManager(BaseUserManager):

    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise AttributeError('Необходимо указать e-mail')
        else:
            email = self.normalize_email(email)

        user = self.model(email=email, first_name = first_name, last_name = last_name, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)  
        return user

    def create_user(self, email, first_name, last_name, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_staffuser(self, email, first_name, last_name, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Для суперпользователя параметр is_staff должен быть True.')
        
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Для суперпользователя параметр is_staff должен быть True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Для суперпользователя параметр is_superuser должен быть True.')

        return self._create_user(email, password, first_name, last_name, **extra_fields)

# Custom User Model

class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name =          'Пользователь'
        verbose_name_plural =   'Пользователи'
    
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT /accounts/user_<id>/<filename>
        return f'accounts/user_{instance.id}/{filename}'

    phone_regex = RegexValidator(regex=r'^\+7\(\d{3,4}\)\d{3}(?:-\d{2}){2}$', 
                                message='Номер телефона ожидается в формате +7(000)000-00-00')

    email =         models.EmailField(
                            _('Email Address'),
                            max_length=255,
                            unique = True,
                            help_text='Нампример: name@hosting.com')

    first_name =    models.CharField(
                            _('first name'), 
                            max_length=150)
    last_name =     models.CharField(
                            _('last name'), 
                            max_length=150)
    image =         models.ImageField(upload_to = user_directory_path,
                            default = 'std/nophoto400.jpg',
                            blank = True,
                            verbose_name='Изображение пользователя')
    job =           models.CharField(
                            max_length=255,
                            verbose_name = 'Должность',
                            blank = True)
    phonenumber =   models.CharField(
                            validators=[phone_regex],
                            max_length = 17,
                            verbose_name = 'Номер телефона',
                            help_text='+7(000)000-00-00 или +7(0000)000-00-00',
                            blank = True,
                            null = True,
                            unique = True)

    is_staff =      models.BooleanField(_('Staff status'), default = False)
    is_active =     models.BooleanField(_('Active'), default = False)
    date_joined =   models.DateTimeField(_('Date Joined'), auto_now_add = True)
    last_updated =  models.DateTimeField(_('Last Updated'), auto_now = True)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_absolute_url(self):
        #return reverse('accounts:profile', kwargs={'user': self.id}) #ссылка на конкретный профиль пока не требуется
        return reverse('accounts:profile')
