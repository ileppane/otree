# Generated by Django 2.2.4 on 2020-06-03 00:35

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('choice_practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='treatment',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]