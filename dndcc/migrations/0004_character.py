# Generated by Django 3.1.2 on 2020-10-17 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndcc', '0003_auto_20201016_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('clss', models.CharField(choices=[('BAR', 'Barbarian'), ('BRD', 'Bard'), ('CLR', 'Cleric'), ('DRD', 'Druid'), ('FTR', 'Fighter'), ('MNK', 'Monk'), ('PAL', 'Paladin'), ('RAN', 'Ranger'), ('ROG', 'Rogue'), ('SRC', 'Sorcerer'), ('WAR', 'Warlock'), ('WIZ', 'Wizard')], max_length=3)),
                ('level', models.IntegerField()),
                ('stn', models.IntegerField(verbose_name='strength')),
                ('dex', models.IntegerField(verbose_name='dexterity')),
                ('con', models.IntegerField(verbose_name='constitution')),
                ('inl', models.IntegerField(verbose_name='intelligence')),
                ('wis', models.IntegerField(verbose_name='wisdom')),
                ('cha', models.IntegerField(verbose_name='charisma')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dndcc.player')),
            ],
            options={
                'ordering': ['level'],
            },
        ),
    ]
