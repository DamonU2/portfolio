# Generated by Django 3.1.2 on 2020-10-13 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='to_do_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.to_do'),
            preserve_default=False,
        ),
    ]
