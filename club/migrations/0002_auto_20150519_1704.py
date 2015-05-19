# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_comment', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id_segment', models.ForeignKey(verbose_name=b'Segment', to='club.Segment', null=True)),
                ('id_story', models.ForeignKey(verbose_name=b'Story', to='club.Story')),
                ('id_user', models.ForeignKey(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='segment',
            name='id_story',
            field=models.ForeignKey(verbose_name=b'Story', to='club.Story'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='closed',
            field=models.BooleanField(default=False, verbose_name=b'Is closed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='public',
            field=models.BooleanField(default=True, verbose_name=b'Is public'),
            preserve_default=True,
        ),
    ]
