# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Date Published')),
                ('aValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bValue', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('siteName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='siteproperties',
            name='relatedSite',
            field=models.ForeignKey(to='demo.Sites'),
        ),
    ]
