# Generated by Django 4.0.2 on 2022-02-12 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0007_gamepicture_base64_gamepicture_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamepicture',
            name='base64',
        ),
        migrations.RemoveField(
            model_name='gamepicture',
            name='player',
        ),
    ]
