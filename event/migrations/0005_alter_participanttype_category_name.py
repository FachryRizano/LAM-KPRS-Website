# Generated by Django 3.2.10 on 2022-01-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_participanttype_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participanttype',
            name='category_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
