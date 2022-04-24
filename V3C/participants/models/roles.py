from django.db import models

class ParticipantRole(models.Model):
    role = models.CharField(max_length=255,
                            unique=True,
                            default='Посетитель')

    def __str__(self):
        return self.role