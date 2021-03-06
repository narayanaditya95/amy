# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 22:31
from __future__ import unicode_literals

from django.db import migrations, models


def add_topics(apps, schema_editor):
    DCWorkshopTopic = apps.get_model('workshops', 'DCWorkshopTopic')

    topics = [
        'Data organization - Ecology spreadsheets, Genomics project '
        'organization or Geospatial introduction to data',
        'Ecology R',
        'Ecology Python',
        'Ecology SQL',
        'Ecology command line',
        'Genomics lessons',
        'Geospatial data lessons',
    ]

    for topic in topics:
        DCWorkshopTopic.objects.create(name=topic)


def add_domains(apps, schema_editor):
    DCWorkshopDomain = apps.get_model('workshops', 'DCWorkshopDomain')

    domains = [
        'Ecology',
        'Genomics',
        'Geospatial data',
    ]

    for domain in domains:
        DCWorkshopDomain.objects.create(name=domain)


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0097_auto_20160617_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCWorkshopTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RunPython(add_topics),
        migrations.CreateModel(
            name='DCWorkshopDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RunPython(add_domains),
    ]
