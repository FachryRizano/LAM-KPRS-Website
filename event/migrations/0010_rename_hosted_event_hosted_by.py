# Generated by Django 3.2.10 on 2021-12-23 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_rename_hosted_by_event_hosted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='hosted',
            new_name='hosted_by',
        ),
    ]