# Generated by Django 2.2.4 on 2020-05-15 20:56

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('REItest', '0006_auto_20200515_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='Intuitiveness_score',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='reflectiveness_score',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]