from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    oauth_token = models.CharField(max_length=100, blank=True)
    oauth_token_secret = models.CharField(max_length=100, blank=True)
    twitter_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.twitter_id

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
