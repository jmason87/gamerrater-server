# Generated by Django 4.0.2 on 2022-02-10 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0003_remove_game_rating_for_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='bio',
        ),
    ]