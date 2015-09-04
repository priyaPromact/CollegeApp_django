# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college_name', models.CharField(max_length=250)),
                ('college_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserCollegeLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('college_id', models.ForeignKey(to='manageApp.College')),
                ('user_id', models.ForeignKey(to='manageApp.Users')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='category_id',
            field=models.ForeignKey(to='manageApp.MainCategories'),
        ),
    ]
