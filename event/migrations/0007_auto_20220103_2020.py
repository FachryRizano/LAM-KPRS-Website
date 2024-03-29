# Generated by Django 3.2.10 on 2022-01-03 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0006_cpd_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpd',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cpd',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='code_registration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participanttype',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
    ]
