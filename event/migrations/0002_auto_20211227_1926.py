# Generated by Django 3.2.10 on 2021-12-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='flyer',
        ),
        migrations.AddField(
            model_name='event',
            name='announcement',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='event_pict',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='logo_organization',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='no_rek',
            field=models.IntegerField(default=0),
        ),
    ]
