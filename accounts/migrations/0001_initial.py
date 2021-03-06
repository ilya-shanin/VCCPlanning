# Generated by Django 4.0.4 on 2022-04-26 14:45

import accounts.models.user
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='Нампример: name@hosting.com', max_length=255, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(help_text='Имя пользователя', max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(help_text='Фамилия пользователя', max_length=150, verbose_name='last name')),
                ('image', models.ImageField(blank=True, upload_to=accounts.models.user.User.user_directory_path)),
                ('job', models.CharField(blank=True, max_length=255, verbose_name='Должность')),
                ('phonenumber', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Номер телефона')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
