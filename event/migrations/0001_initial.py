# Generated by Django 3.2.10 on 2021-12-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal', models.DateTimeField()),
                ('tempat', models.CharField(max_length=100)),
                ('hosted_by', models.CharField(max_length=100)),
                ('organized_by', models.CharField(max_length=100)),
                ('event_website', models.CharField(max_length=200)),
                ('flyer', models.CharField(max_length=200)),
                ('harga', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
