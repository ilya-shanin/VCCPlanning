# Generated by Django 4.0.4 on 2022-04-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Имя пользователя', max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Фамилия пользователя', max_length=150, verbose_name='last name'),
        ),
    ]
