# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0002_auto_20150919_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeappuser',
            name='username',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
