# Generated by Django 3.0 on 2022-06-29 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='role',
            new_name='player_name',
        ),
    ]