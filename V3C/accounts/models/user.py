
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """ User manager """

    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not email:  # check for an empty email
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email
            email = self.normalize_email(email)

        # create user
        user = self.model(email=email, first_name = first_name, last_name = last_name, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        return user

    def create_user(self, password, email, first_name, last_name, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_staffuser(self, password, email, first_name, last_name, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, password, email, first_name, last_name, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def get_by_natural_key(self, email_):
        return self.get(email = email_)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name = 'Пользователи'
    
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return f'user_{instance.user.id}/{filename}'

    email =         models.EmailField(
                            _("Email Address"),
                            max_length=255,
                            unique=True,
                            help_text="Нампример: name@hosting.com")
    #password =      models.CharField(
    #                        _('password'),
    #                        max_length=255,
    #                        help_text='Пароль')
    first_name =    models.CharField(
                            _('first name'), 
                            max_length=150,
                            help_text="Ваше имя")
    last_name =     models.CharField(
                            _('last name'), 
                            max_length=150,
                            help_text="Ваша фамилия")
    image =         models.ImageField(upload_to = user_directory_path,
                                      blank = True)
    job =           models.CharField(
                            max_length=255,
                            verbose_name = 'Должность',
                            blank = True)
    phonenumber =   models.CharField(
                            max_length = 15,
                            verbose_name = 'Номер телефона',
                            blank = True)

    is_staff =      models.BooleanField(_("Staff status"), default=False)
    is_active =     models.BooleanField(_("Active"), default=True)
    date_joined =   models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated =  models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'user': self.email})
