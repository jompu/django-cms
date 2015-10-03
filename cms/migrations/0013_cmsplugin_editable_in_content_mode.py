# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsplugin',
            name='editable_in_content_mode',
            field=models.BooleanField(default=True, verbose_name='Is editable in content mode.'),
        ),
    ]
