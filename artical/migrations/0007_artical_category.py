# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0006_artical_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='category',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
