# Generated by Django 2.2.4 on 2020-04-15 15:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('funnel', '0006_auto_20200415_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='x',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='y',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]