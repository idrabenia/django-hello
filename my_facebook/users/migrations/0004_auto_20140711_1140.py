# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20140711_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='street',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='address',
            name='address2',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='address3',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
