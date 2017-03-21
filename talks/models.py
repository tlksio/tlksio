from django.db import models


class Talk(models.Model):
    # id
    code = models.CharField(max_length=25)
    # slug
    title = models.TextField()
    speaker = models.CharField(max_length=100)
    # author
    description = models.TextField()
    # tags
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    view_count = models.IntegerField('view count')
    vote_count = models.IntegerField('vote count')
    # votes
    fav_count = models.IntegerField('favorite count')
    # favorites
    # ranking
    # type
