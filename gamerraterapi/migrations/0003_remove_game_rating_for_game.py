# Generated by Django 4.0.2 on 2022-02-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0002_game_rating_for_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rating_for_game',
        ),
    ]
