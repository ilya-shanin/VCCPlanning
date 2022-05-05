from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

class EventAbstract(models.Model):
    #day = models.DateField(verbose_name='Дата', 
    #                       help_text = 'Дата события')
    start_time =    models.DateTimeField(
                                        verbose_name='Начинается в', 
                                        help_text = 'Время начала')
    end_time =      models.DateTimeField(
                                        verbose_name='Заканчивается в', 
                                        help_text = 'Время окончания (необязательно)',
                                        null=True,
                                        blank=True)
    notes =         models.TextField(
                                    verbose_name='Примечание', 
                                    help_text = 'Максимум 1000 символов  (необязательно)', 
                                    max_length=1000,
                                    blank=True)

    is_active =     models.BooleanField(_("Active"), default=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True