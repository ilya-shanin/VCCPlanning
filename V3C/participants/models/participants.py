from django.db import models
from events.models import Conference
from participants.models import ParticipantRole
from django.conf import settings
import datetime

class ParticipantManager(models.Manager):
    def get_all_user_events(self, user):
        events = Participant.objects.filter(user__id = user.id)
        return events

    def get_running_events(self, user):
        events = Participant.objects.filter(user__id = user.id, 
                                            event__is_active = True, 
                                            event__start_time__gte = datetime.datetime.now())
        return events

    def get_event_participants(self, event_id):
        participants = Participant.objects.filter(event__pk = event_id)
        return participants

class Participant(models.Model):

    
    event = models.ForeignKey(
                            Conference, 
                            on_delete=models.CASCADE, 
                            related_name='rel_conf',
                            verbose_name='Событие')
    user =  models.ForeignKey(
                            settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE, 
                            related_name='rel_users',
                            verbose_name='Пользователь')
    role =  models.ForeignKey(
                            ParticipantRole, 
                            on_delete=models.PROTECT, 
                            related_name='rel_roles',
                            verbose_name='Роль участника')

    objects = ParticipantManager()

    class Meta:
        verbose_name =          'Участник'
        verbose_name_plural =   'Участники'

        unique_together = ['user', 'event']

    def __str__(self):
        return f'{self.event}, {self.user}'
        