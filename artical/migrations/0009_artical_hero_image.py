# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artical.models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='hero_image',
            field=models.FileField(default=0, upload_to=artical.models.get_upload_file_name),
        ),
    ]
