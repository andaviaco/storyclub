# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('id_user', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('role', models.CharField(default=b'D', max_length=1, verbose_name=b'User role', choices=[(b'A', b'Admin'), (b'M', b'Moderator'), (b'D', b'Default')])),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id_segment', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=512)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_last', models.BooleanField(default=False)),
                ('proposed_end', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id_story', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=254)),
                ('first_text', models.TextField(max_length=1024)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='segment',
            name='id_story',
            field=models.ForeignKey(to='club.Story'),
            preserve_default=True,
        ),
    ]
