from django.db import models

class ParticipantRole(models.Model):
    class Meta:
        verbose_name =          'Роль в конференции'
        verbose_name_plural =   'Роли в конференции'

    role = models.CharField(
                            max_length=255,
                            verbose_name='Роль',
                            unique=True,
                            default='Посетитель')

    def __str__(self):
        return self.role