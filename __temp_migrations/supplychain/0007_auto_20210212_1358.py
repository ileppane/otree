# Generated by Django 2.2.12 on 2021-02-12 13:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychain', '0006_auto_20210211_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='rprofit',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='wprofit',
            field=otree.db.models.FloatField(null=True),
        ),
    ]