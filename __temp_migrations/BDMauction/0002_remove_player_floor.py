# Generated by Django 2.2.4 on 2020-06-12 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BDMauction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='floor',
        ),
    ]
