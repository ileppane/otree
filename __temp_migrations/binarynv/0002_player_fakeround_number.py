# Generated by Django 2.2.12 on 2021-09-30 12:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('binarynv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fakeround_number',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]