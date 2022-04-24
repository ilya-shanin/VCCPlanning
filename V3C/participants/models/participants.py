from django.db import models
from events.models import Conference
from participants.models import ParticipantRole
from django.conf import settings

class Participant(models.Model):

    
    event = models.ForeignKey(Conference, 
                                on_delete=models.CASCADE, 
                                related_name='name',
                                verbose_name='Событие')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name='email',
                                verbose_name='Пользователь')
    role = models.ForeignKey(ParticipantRole, 
                             on_delete=models.PROTECT, 
                             related_name='role',
                             verbose_name='Роль участника')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

        unique_together = ['user', 'event']

    def __str__(self):
        return f'{self.event}, {self.user}'