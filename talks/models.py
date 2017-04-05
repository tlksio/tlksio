import json
import urllib.request

from django.db import models

from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils.text import slugify


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
    code = models.CharField(max_length=25, unique=True, null=False, blank=False, default=None)
    title = models.CharField(max_length=200, null=False, blank=False, default=None)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    description = models.TextField(blank=True)
    tags = TaggableManager()
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    view_count = models.PositiveIntegerField('view count', default=0)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='youtube')
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    votes = models.ManyToManyField(User, blank=True, related_name='votes')
    thumbnail = models.URLField('video thumbnail', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            if Talk.objects.filter(slug=self.slug).count() > 0:
                self.slug = self.slug + "-" + self.code

        # Get video thubnail with an additional API call if it is a vimeo
        # video.
        if self.type == 'vimeo':
            raw_data = urllib.request.urlopen("https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/"+self.code).read()
            data = json.loads(raw_data.decode("utf-8"))
            self.thumbnail = data['thumbnail_url']

        super(Talk, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Talk"
        verbose_name_plural = "Talks"
        get_latest_by = "-created"
        ordering = ['-created', '-updated']

