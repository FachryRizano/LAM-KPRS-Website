# Generated by Django 3.2.10 on 2022-01-03 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_participanttype_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpd',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
    ]