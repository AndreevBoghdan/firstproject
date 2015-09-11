# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150803_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name=b'New Comment'),
        ),
    ]
