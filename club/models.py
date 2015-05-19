# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

class Story(models.Model):
    id_story = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    first_text = models.TextField(max_length=1024)
    publish_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return '{}'.format(self.title)


class Segment(models.Model):
    id_segment = models.AutoField(primary_key=True)
    text = models.TextField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)
    is_last = models.BooleanField(default=False)
    proposed_end = models.BooleanField(default=False)
    id_story = models.ForeignKey(Story)

    def __unicode__(self):
        return '{} <{}>'.format(self.text[:50], self.date)
