# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artical.models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0014_auto_20151008_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='optional_image',
            field=models.FileField(null=True, upload_to=artical.models.get_upload_file_name, blank=True),
        ),
    ]
