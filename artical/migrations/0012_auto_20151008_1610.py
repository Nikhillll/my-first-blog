# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artical', '0011_auto_20151008_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
