# Generated by Django 3.2.10 on 2021-12-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20211228_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
