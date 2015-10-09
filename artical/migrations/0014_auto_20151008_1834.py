# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0013_auto_20151008_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.TextField(default=b'None'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(default=b'Guest', max_length=50),
        ),
    ]
