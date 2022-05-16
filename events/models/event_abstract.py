from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

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

    def live(self):
        now = datetime.datetime.now().timestamp()
        if self.end_time and self.start_time.timestamp() <= now <= self.end_time.timestamp():
            return True
        else: return False

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})