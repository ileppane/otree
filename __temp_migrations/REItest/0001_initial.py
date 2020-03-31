# Generated by Django 2.2.4 on 2020-03-30 18:21

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reitest_group', to='otree.Session')),
            ],
            options={
                'db_table': 'REItest_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reitest_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'REItest_subsession',
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
                ('nfcscore', otree.db.models.PositiveIntegerField(null=True)),
                ('fiscore', otree.db.models.PositiveIntegerField(null=True)),
                ('q1', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q2', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q3', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q4', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q5', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q6', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q7', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q8', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q9', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q10', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q11', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q12', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q13', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q14', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q15', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q16', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q17', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q18', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q19', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q20', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q21', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q22', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q23', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q24', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q25', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q26', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q27', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q28', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q29', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q30', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('q31', otree.db.models.PositiveIntegerField(choices=[[1, '1 = definitely not true'], [2, '2 = somewhat not true'], [3, '3 = neither true nor untrue'], [4, '4 = somewhat true'], [5, '5 = definitely true']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='REItest.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reitest_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reitest_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='REItest.Subsession')),
            ],
            options={
                'db_table': 'REItest_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='REItest.Subsession'),
        ),
    ]
