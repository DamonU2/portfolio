# Generated by Django 3.1.2 on 2020-10-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndcc', '0007_weapon_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='bonus',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='mod',
            field=models.CharField(choices=[('stn', 'Strength'), ('dex', 'Dexterity')], max_length=3),
        ),
    ]
