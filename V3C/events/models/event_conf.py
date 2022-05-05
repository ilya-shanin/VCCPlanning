from django.db import models
from events.models import EventAbstract
import datetime

class ConferenceManager(models.Manager):
    pass

class Conference(EventAbstract):
    name =              models.CharField(
                                        verbose_name='Конференция', 
                                        help_text = 'Наименование конференции', 
                                        max_length = 255, 
                                        unique=True)
    con_reference =     models.CharField(
                                        verbose_name='Ссылка на конференцию',
                                        help_text='Адрес для подкючения к конференции',
                                        max_length=255,
                                        blank=True,
                                        default='Ссылка для подключения пока не указана')
    con_pass =          models.CharField(
                                        verbose_name='Пароль для входа в конференцию',
                                        help_text='Пароль для входа (Необязательно). Не более 255 символов.',
                                        max_length=255,
                                        blank=True,
                                        default='Не требуется')

    class Meta:
        verbose_name =          'Конференция'
        verbose_name_plural =   'Конференции'

    def __str__(self):
        return self.name