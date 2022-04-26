# Generated by Django 4.0.4 on 2022-04-26 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='Посетитель', max_length=255, unique=True, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Роль в конференции',
                'verbose_name_plural': 'Роли в конференции',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='events.conference', verbose_name='Событие')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='participants.participantrole', verbose_name='Роль участника')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
                'unique_together': {('user', 'event')},
            },
        ),
    ]
