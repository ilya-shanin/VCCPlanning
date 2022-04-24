#from __future__ import unicode_literals

from tabnanny import verbose
from django.db import models

class Event(models.Model):
    name = models.CharField(verbose_name='Конференция', 
                            help_text = 'Наименование конференции', 
                            max_length = 255, 
                            unique=True)
    #day = models.DateField(verbose_name='Дата', 
    #                       help_text = 'Дата события')
    start_time = models.DateTimeField(verbose_name='Начинается в', 
                                  help_text = 'Время начала')
    end_time = models.DateTimeField(verbose_name='Заканчивается в', 
                                help_text = 'Время окончания (необязательно)',
                                null=True,
                                blank=True)
    con_reference = models.CharField(verbose_name='Ссылка на конференцию',
                                    help_text='Адрес для подкючения к конференции',
                                    max_length=255,
                                    blank=True,
                                    default='Ссылка для подключения пока не указана')
    con_pass = models.CharField(verbose_name='Пароль для входа в конференцию',
                                help_text='Пароль для входа (Необязательно). Не более 255 символов.',
                                max_length=255,
                                blank=True,
                                default='Не требуется')
    notes = models.TextField(verbose_name='Примечание', 
                             help_text = 'Максимум 1000 символов  (необязательно)', 
                             max_length=1000,
                             blank=True)

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'