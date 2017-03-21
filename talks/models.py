from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User

class Talk(models.Model):
    # id
    code = models.CharField(max_length=25)
    # slug
    title = models.TextField()
    speaker = models.CharField(max_length=100)
    # author
    description = models.TextField()
    tags = TaggableManager()
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    view_count = models.IntegerField('view count')
    vote_count = models.IntegerField('vote count')
    fav_count = models.IntegerField('favorite count')
    # ranking
    # type


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)