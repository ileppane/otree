# Generated by Django 2.2.4 on 2020-05-05 21:03

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moonrover_group', to='otree.Session')),
            ],
            options={
                'db_table': 'moonrover_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moonrover_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'moonrover_subsession',
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
                ('startx', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], null=True)),
                ('starty', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], null=True)),
                ('firstsite', otree.db.models.StringField(choices=[('Barking', 'Barking'), ('Pier', 'Pier'), ('Shooters Hill', 'Shooters Hill'), ('East Ham', 'East Ham'), ('Beckton', 'Beckton'), ('Woolwich', 'Woolwich'), ('Greenwich', 'Greenwich'), ('Millwall', 'Millwall'), ('Bow', 'Bow'), ('Stratford', 'Stratford')], max_length=10000, null=True)),
                ('secondsite', otree.db.models.StringField(choices=[('Barking', 'Barking'), ('Pier', 'Pier'), ('Shooters Hill', 'Shooters Hill'), ('East Ham', 'East Ham'), ('Beckton', 'Beckton'), ('Woolwich', 'Woolwich'), ('Greenwich', 'Greenwich'), ('Millwall', 'Millwall'), ('Bow', 'Bow'), ('Stratford', 'Stratford')], max_length=10000, null=True)),
                ('thirdsite', otree.db.models.StringField(choices=[('Barking', 'Barking'), ('Pier', 'Pier'), ('Shooters Hill', 'Shooters Hill'), ('East Ham', 'East Ham'), ('Beckton', 'Beckton'), ('Woolwich', 'Woolwich'), ('Greenwich', 'Greenwich'), ('Millwall', 'Millwall'), ('Bow', 'Bow'), ('Stratford', 'Stratford')], max_length=10000, null=True)),
                ('fourthsite', otree.db.models.StringField(choices=[('Barking', 'Barking'), ('Pier', 'Pier'), ('Shooters Hill', 'Shooters Hill'), ('East Ham', 'East Ham'), ('Beckton', 'Beckton'), ('Woolwich', 'Woolwich'), ('Greenwich', 'Greenwich'), ('Millwall', 'Millwall'), ('Bow', 'Bow'), ('Stratford', 'Stratford')], max_length=10000, null=True)),
                ('points', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moonrover.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moonrover_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moonrover_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moonrover.Subsession')),
            ],
            options={
                'db_table': 'moonrover_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moonrover.Subsession'),
        ),
    ]