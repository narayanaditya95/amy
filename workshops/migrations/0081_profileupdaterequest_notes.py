# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0080_award_awarded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileupdaterequest',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
