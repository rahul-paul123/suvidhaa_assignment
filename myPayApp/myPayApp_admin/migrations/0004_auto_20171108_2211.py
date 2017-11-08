# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-08 22:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myPayApp_admin', '0003_auto_20171108_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billerprofile',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='billerprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='billerprofile',
            name='mypayappuser_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
