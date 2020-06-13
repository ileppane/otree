# Generated by Django 2.2.4 on 2020-06-12 20:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BDMauction', '0003_auto_20200612_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cq_l3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$30'], [2, '$70'], [3, '$10'], [4, '$25']], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='cq_l2',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '30%'], [2, '70%'], [3, '10%'], [4, '25%']], null=True),
        ),
    ]