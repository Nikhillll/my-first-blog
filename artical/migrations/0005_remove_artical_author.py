# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0004_artical_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical',
            name='author',
        ),
    ]
