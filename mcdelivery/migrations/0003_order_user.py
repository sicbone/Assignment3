# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('mcdelivery', '0002_auto_20150727_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
