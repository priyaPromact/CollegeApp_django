# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0002_auto_20150627_1223'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='collegeAppUser',
        ),
    ]
