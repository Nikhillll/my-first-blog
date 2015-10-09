# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0003_auto_20151005_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='author',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
