from django.db import models
from events.models import Conference
from participants.models import ParticipantRole
from django.conf import settings
import datetime
from django.utils import timezone

class ParticipantManager(models.Manager):
    def get_all_user_events(self, user):
        events = Participant.objects.filter(user__id = user.id)
        return events

    def get_running_events(self, user):
        events = Participant.objects.filter(user__id = user.id, 
                                            event__is_active = True, 
                                            event__start_time__lte = datetime.datetime.now()
                                            )
        return events

    def get_planned_events(self, user):
        events = Participant.objects.filter(user__id = user.id, 
                                            event__is_active = True, 
                                            event__start_time__gte = datetime.datetime.now()
                                            )
        return events

    def get_today_events(self, user):
        events = Participant.objects.filter(user__id = user.id, 
                                            event__is_active = True, 
                                            event__start_time__gte=timezone.now().replace(hour=0, minute=0, second=0), 
                                            event__end_time__lte=timezone.now().replace(hour=23, minute=59, second=59)
                                            )
        return events

    def get_day_events(self, user, day):
        events = Participant.objects.filter(user__id = user.id, 
                                            event__is_active = True, 
                                            event__start_time__gte=day.replace(hour=0, minute=0, second=0), 
                                            event__end_time__lte=day.replace(hour=23, minute=59, second=59)
                                            )
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
        ordering = ['event__start_time']
        unique_together = ['user', 'event']

    def __str__(self):
        return f'{self.event}, {self.user}'
        