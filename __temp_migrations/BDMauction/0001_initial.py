# Generated by Django 2.2.12 on 2021-04-10 16:37

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bdmauction_group', to='otree.Session')),
            ],
            options={
                'db_table': 'BDMauction_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bdmauction_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'BDMauction_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('treatment', otree.db.models.StringField(max_length=10000, null=True)),
                ('WTP', otree.db.models.FloatField(null=True)),
                ('jsdectime_start', otree.db.models.FloatField(null=True)),
                ('jsdectime_end', otree.db.models.FloatField(null=True)),
                ('jsdectime', otree.db.models.FloatField(null=True)),
                ('reward', otree.db.models.FloatField(null=True)),
                ('risk', otree.db.models.FloatField(null=True)),
                ('payoff_auc', otree.db.models.LongStringField(null=True)),
                ('cq_l1', otree.db.models.PositiveIntegerField(choices=[[1, '30%'], [2, '70%'], [3, '10%'], [4, '25%']], null=True)),
                ('cq_l2', otree.db.models.PositiveIntegerField(choices=[[1, '30%'], [2, '70%'], [3, '10%'], [4, '25%']], null=True)),
                ('cq_l3', otree.db.models.PositiveIntegerField(choices=[[1, '$30'], [2, '$70'], [3, '$10'], [4, '$25']], null=True)),
                ('cq_a1', otree.db.models.PositiveIntegerField(choices=[[1, '$25'], [2, '$35'], [3, '$16'], [4, 'None of the above']], null=True)),
                ('cq_a2', otree.db.models.PositiveIntegerField(choices=[[1, '$19'], [2, '$29'], [3, '$31'], [4, '$21']], null=True)),
                ('cq_a3', otree.db.models.PositiveIntegerField(choices=[[1, '$19'], [2, '$29'], [3, '$31'], [4, '$21']], null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BDMauction.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bdmauction_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bdmauction_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BDMauction.Subsession')),
            ],
            options={
                'db_table': 'BDMauction_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BDMauction.Subsession'),
        ),
    ]
