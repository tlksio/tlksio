from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oauth_token = models.CharField(max_length=100, blank=True)
    oauth_token_secret = models.CharField(max_length=100, blank=True)
    twitter_id = models.CharField(max_length=100, blank=True)
    avatar = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.twitter_id

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Talk(models.Model):
    TYPE_CHOICES = (
        ('youtube', 'Youtube'),
        ('vimeo', 'Vimeo'),
    )
    code = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    tags = TaggableManager()
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    view_count = models.PositiveIntegerField('view count')
    vote_count = models.PositiveIntegerField('vote count')
    fav_count = models.PositiveIntegerField('favorite count')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='youtube')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Talk"
        verbose_name_plural = "Talks"
        get_latest_by = "-created"
        ordering = ['-created', '-updated']


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
