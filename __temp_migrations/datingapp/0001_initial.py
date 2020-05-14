# Generated by Django 2.2.4 on 2020-05-05 19:22

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datingapp_group', to='otree.Session')),
            ],
            options={
                'db_table': 'datingapp_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datingapp_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'datingapp_subsession',
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
                ('name', otree.db.models.StringField(max_length=10000, null=True)),
                ('Jack', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Thomas', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('James', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Joshua', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Daniel', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Harry', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Samuel', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Joseph', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Matthew', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('Callum', otree.db.models.StringField(choices=[('Chloe', 'Chloe'), ('Emily', 'Emily'), ('Megan', 'Megan'), ('Charlotte', 'Charlotte'), ('Jessica', 'Jessica'), ('Lauren', 'Lauren'), ('Sophie', 'Sophie'), ('Olivia', 'Olivia'), ('Hannah', 'Hannah'), ('Lucy', 'Lucy')], max_length=10000, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datingapp.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datingapp_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datingapp_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingapp.Subsession')),
            ],
            options={
                'db_table': 'datingapp_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datingapp.Subsession'),
        ),
    ]