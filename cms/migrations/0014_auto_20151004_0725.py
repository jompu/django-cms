# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_cmsplugin_editable_in_content_mode'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('reverse_id', 'site', 'publisher_is_draft'), ('publisher_is_draft', 'site', 'application_namespace')]),
        ),
    ]
