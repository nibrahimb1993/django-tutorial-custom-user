# Generated by Django 3.1.2 on 2020-10-10 08:05

from django.db import migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('options', profiles.models.UserManager()),
            ],
        ),
    ]