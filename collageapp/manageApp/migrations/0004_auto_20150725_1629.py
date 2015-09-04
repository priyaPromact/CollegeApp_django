# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0003_auto_20150725_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategoryLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat', models.ForeignKey(to='manageApp.MainCategories')),
                ('user', models.ForeignKey(to='manageApp.collegeAppUser')),
            ],
        ),
        migrations.RenameField(
            model_name='usercollegelink',
            old_name='college_id',
            new_name='college',
        ),
        migrations.RenameField(
            model_name='usercollegelink',
            old_name='user_id',
            new_name='user',
        ),
    ]
