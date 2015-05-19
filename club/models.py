# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


USER_ROLES = (
    ('A', 'Admin'),
    ('M', 'Moderator'),
    ('D', 'Default'),
)

ADMIN_USER = 'A'
MOD_USER = 'M'
COMMON_USER = 'D'

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username.')

        if not kwargs.get('email'):
            raise ValueError('Users must have a valid email address.')

        user = self.model(
            email=self.normalize_email(kwargs.get('email')), username=username
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username, password, **kwargs)

        user.role = ADMIN_USER
        user.save()

        return user

class User(AbstractBaseUser):
    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    role = models.CharField('User role', max_length=1, choices=USER_ROLES, default=COMMON_USER)

    registered_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return '{} <{}>'.format(self.username, self.email)

    def get_full_name(self):
        return '{} <{}>'.format(self.username, self.email)

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        if self.role == ADMIN_USER:
            return True
        return False


class Story(models.Model):
    id_story = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    first_text = models.TextField(max_length=1024)
    publish_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False, verbose_name='Is closed')
    public = models.BooleanField(default=True, verbose_name='Is public')
    users = models.ManyToManyField(User, through='UsersRelStories', verbose_name='Related users')

    def __unicode__(self):
        return '{}'.format(self.title)


class Segment(models.Model):
    id_segment = models.AutoField(primary_key=True)
    text = models.TextField(max_length=512)
    date = models.DateTimeField(auto_now_add=True)
    is_last = models.BooleanField(default=False)
    proposed_end = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='UsersRelSegments', verbose_name='Related users')
    id_story = models.ForeignKey(Story, verbose_name='Story')

    def __unicode__(self):
        return '{} <{}>'.format(self.text[:50], self.date)


class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, verbose_name='User')
    id_segment = models.ForeignKey(Segment, verbose_name='Segment', null=True)
    id_story = models.ForeignKey(Story, verbose_name='Story')

    def __unicode__(self):
        return '{}'.format(self.text[:50])


class UsersRelStories(models.Model):
    id_user = models.ForeignKey(User, verbose_name='User')
    id_story = models.ForeignKey(Story, verbose_name='Story')
    favorite = models.BooleanField(default=False)
    following = models.BooleanField(default=False)
    author = models.BooleanField(default=False)
    contribution = models.BooleanField(default=False)
    can_contribute = models.BooleanField(default=True)


class UsersRelSegments(models.Model):
    id_user = models.ForeignKey(User, verbose_name='User')
    id_segment = models.ForeignKey(Segment, verbose_name='Segment')
    author = models.BooleanField(default=True)
    vote = models.NullBooleanField(default=False, blank=True)
