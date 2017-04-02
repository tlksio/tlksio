#!/usr/bin/env python

import os
import sys
import django
from datetime import datetime

from django.db import IntegrityError
from django.utils.text import slugify

from django.utils import timezone

sys.path.append("/home/raul/tlksio")
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

from pymongo import MongoClient
client = MongoClient('mongodb://import:import@ds043180.mlab.com:43180/techtalks')

from talks.models import Profile
Profile.objects.all().delete()
from django.contrib.auth.models import User
all_users = client.techtalks.users.find({})
for user in all_users:
    try:
        obj = User.objects.get(username=user['username'])
    except User.DoesNotExist:
        obj = User(username=user['username'])
        obj.save()

    try:
        pobj = Profile.objects.get(twitter_id=user['twitterId'])
    except Profile.DoesNotExist:
        pobj = Profile(user=obj)
        pobj.twitter_id = user['twitterId']
        pobj.bio = user['bio']
        pobj.avatar = user['avatar']
        pobj.save()

from taggit.models import Tag
Tag.objects.all().delete()
from talks.models import Talk
Talk.objects.all().delete()
"""
from talks.models import Favorite
Favorite.objects.all().delete()
from talks.models import Vote
Vote.objects.all().delete()
"""
all_talks = client.techtalks.talks.find({})
for talk in all_talks:
    t = Talk()
    t.code = talk['code']
    t.title = talk['title']
    t.slug = talk['slug']
    t.description = talk['description']
    t.type = talk['type']
    t.view_count = talk['viewCount']
    t.vote_count = talk['voteCount']
    t.fav_count = talk['favoriteCount']
    t.author = User.objects.get(username=talk['author']['username'])
    dt = datetime.utcfromtimestamp(talk['created']/1000.0)
    dt_aware = timezone.make_aware(dt, timezone.get_current_timezone())
    t.created = dt_aware
    t.updated = dt_aware
    t.save()

    for tag in talk['tags']:
        slug = slugify(tag)
        try:
            obj = Tag.objects.get(slug=slug)
        except Tag.DoesNotExist:
            obj = Tag(name=tag, slug=slug)
            try:
                obj.save()
            except IntegrityError:
                obj.slug=slug+"-"+t.code
                obj.save()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        t.tags.add(tag)

    for favorite in talk['favorites']:
        u = client.techtalks.users.find_one({"id": favorite})
        if not u:
            break
        uu = User.objects.get(username=u['username'])
        t.favorites.add(uu)

    for vote in talk['votes']:
        u = client.techtalks.users.find_one({"id": vote})
        if not u:
            break
        uu = User.objects.get(username=u['username'])
        t.votes.add(uu)

    t.save()

    print('.', end='', flush=True)
