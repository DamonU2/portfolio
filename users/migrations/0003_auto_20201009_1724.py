# Generated by Django 3.1.2 on 2020-10-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201009_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users/default.jpg', upload_to='users/profile_pics'),
        ),
    ]