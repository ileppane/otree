# Generated by Django 2.2.12 on 2021-02-11 19:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('supplychain', '0003_auto_20210211_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='retaileraccept',
            field=otree.db.models.IntegerField(null=True, verbose_name=''),
        ),
    ]