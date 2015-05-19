# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20150519_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersRelSegments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.BooleanField(default=True)),
                ('vote', models.NullBooleanField(default=False)),
                ('id_segment', models.ForeignKey(verbose_name=b'Segment', to='club.Segment')),
                ('id_user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsersRelStories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite', models.BooleanField(default=False)),
                ('following', models.BooleanField(default=False)),
                ('author', models.BooleanField(default=False)),
                ('contribution', models.BooleanField(default=False)),
                ('can_contribute', models.BooleanField(default=True)),
                ('id_story', models.ForeignKey(verbose_name=b'Story', to='club.Story')),
                ('id_user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='segment',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Related users', through='club.UsersRelSegments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Related users', through='club.UsersRelStories'),
            preserve_default=True,
        ),
    ]
