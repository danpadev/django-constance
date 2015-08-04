# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constance',
            name='key',
            field=models.CharField(unique=True, max_length=255, verbose_name='key'),
        ),
        migrations.AlterField(
            model_name='constance',
            name='value',
            field=picklefield.fields.PickledObjectField(verbose_name='value', editable=False),
        ),
    ]
