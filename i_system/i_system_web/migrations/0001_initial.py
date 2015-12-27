# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_arms', models.IntegerField(default=0)),
                ('name_arms', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_calls', models.IntegerField(default=0)),
                ('nambe_calls', models.IntegerField(default=0)),
                ('date_calls', models.DateTimeField(verbose_name=b'date published')),
                ('description_calls', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cats', models.IntegerField(default=0)),
                ('name_cats', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Departs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_dep', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_equip', models.IntegerField(default=0)),
                ('name_equip', models.CharField(max_length=100)),
                ('invert_nambe', models.IntegerField(default=0)),
                ('departs', models.ForeignKey(to='i_system_web.Departs')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idposts', models.IntegerField(default=0)),
                ('name_post', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rel_types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_rel_types', models.CharField(max_length=100)),
                ('id_rel_types', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_relatives', models.IntegerField(default=0)),
                ('date_relatives', models.DateTimeField(verbose_name=b'date published')),
                ('description_relatives', models.CharField(max_length=200)),
                ('equip', models.ForeignKey(to='i_system_web.Equip')),
                ('rel_types', models.ForeignKey(to='i_system_web.Rel_types')),
            ],
        ),
        migrations.CreateModel(
            name='Repairs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_repairs', models.IntegerField(default=0)),
                ('nambe_repairs', models.IntegerField(default=0)),
                ('start_date_repairs', models.DateTimeField(verbose_name=b'date published')),
                ('finish_date_repairs', models.DateTimeField(verbose_name=b'date published')),
                ('text_problem', models.CharField(max_length=300)),
                ('equip', models.ForeignKey(to='i_system_web.Equip')),
            ],
        ),
        migrations.CreateModel(
            name='Types1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_types', models.IntegerField(default=0)),
                ('name_types', models.CharField(max_length=60)),
                ('manufacturer', models.CharField(max_length=60)),
                ('order_name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('note', models.CharField(max_length=250)),
                ('cats', models.ForeignKey(to='i_system_web.Cats')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idusers', models.IntegerField(default=0)),
                ('fio', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('departs', models.ForeignKey(to='i_system_web.Departs')),
                ('posts', models.ForeignKey(to='i_system_web.Posts')),
            ],
        ),
        migrations.AddField(
            model_name='repairs',
            name='users',
            field=models.ForeignKey(to='i_system_web.Users'),
        ),
        migrations.AddField(
            model_name='relatives',
            name='users',
            field=models.ForeignKey(to='i_system_web.Users'),
        ),
        migrations.AddField(
            model_name='calls',
            name='equip',
            field=models.ForeignKey(to='i_system_web.Equip'),
        ),
        migrations.AddField(
            model_name='calls',
            name='users',
            field=models.ForeignKey(to='i_system_web.Users'),
        ),
        migrations.AddField(
            model_name='arms',
            name='users',
            field=models.ForeignKey(to='i_system_web.Users'),
        ),
    ]
