# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
