# Generated by Django 2.2.12 on 2021-08-12 20:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ECI_survey', '0014_auto_20210812_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='randomnumber',
            field=otree.db.models.FloatField(null=True),
        ),
    ]