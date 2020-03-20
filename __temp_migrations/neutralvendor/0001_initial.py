# Generated by Django 2.2.4 on 2020-03-20 14:42

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neutralvendor_group', to='otree.Session')),
            ],
            options={
                'db_table': 'neutralvendor_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neutralvendor_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'neutralvendor_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('starttime', otree.db.models.FloatField(null=True)),
                ('endtime', otree.db.models.FloatField(null=True)),
                ('decision', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True)),
                ('state', otree.db.models.PositiveIntegerField(null=True)),
                ('truestate', otree.db.models.StringField(max_length=10000, null=True)),
                ('truedecision', otree.db.models.StringField(max_length=10000, null=True)),
                ('check1', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '936'], [2, '364'], [3, '858']], null=True)),
                ('check2', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '0'], [2, '1/7'], [3, '5/7']], null=True)),
                ('check3', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], null=True)),
                ('check4', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '1/7'], [2, '0'], [3, '5/7']], null=True)),
                ('check5', otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '£0.11'], [2, '£11.30'], [3, '£1.13']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neutralvendor.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neutralvendor_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neutralvendor_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neutralvendor.Subsession')),
            ],
            options={
                'db_table': 'neutralvendor_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neutralvendor.Subsession'),
        ),
    ]
