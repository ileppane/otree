# Generated by Django 2.2.4 on 2020-05-21 20:42

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cognitivenoise', '0009_auto_20200520_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='treatment',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
