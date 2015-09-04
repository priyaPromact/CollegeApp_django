# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0004_auto_20150725_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeCategoryLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_id', models.ForeignKey(to='manageApp.MainCategories')),
            ],
        ),
        migrations.RemoveField(
            model_name='college',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='collegeappuser',
            name='oAuthID',
        ),
        migrations.AddField(
            model_name='collegecategorylink',
            name='college_id',
            field=models.ForeignKey(to='manageApp.College'),
        ),
    ]
