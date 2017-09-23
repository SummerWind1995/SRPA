# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 08:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('const', '0003_workshop_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('target_uid', models.UUIDField(verbose_name='被审阅对象')),
                ('desc', models.TextField(verbose_name='意见')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='审阅人')),
            ],
            options={
                'verbose_name': '审阅意见',
                'verbose_name_plural': '审阅意见',
            },
        ),
    ]