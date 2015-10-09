# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0012_auto_20151008_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
