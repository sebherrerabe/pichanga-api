# Generated by Django 3.0 on 2022-07-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220629_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='live_time',
        ),
    ]
