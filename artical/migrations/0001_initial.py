# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
