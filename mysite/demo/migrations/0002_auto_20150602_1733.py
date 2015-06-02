# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteproperties',
            name='date',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
    ]
