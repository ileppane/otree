# Generated by Django 2.2.4 on 2020-06-03 23:57

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cognitivenoise', '0013_player_pyresttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='pay',
        ),
        migrations.AddField(
            model_name='player',
            name='payoff_ddm',
            field=otree.db.models.LongStringField(null=True),
        ),
    ]
