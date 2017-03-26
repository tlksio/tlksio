from django.contrib import admin

from .models import Talk
"""
from .models import Vote
from .models import Favorite
"""
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'twitter_id']

admin.site.register(Profile, ProfileAdmin)


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ['created', 'type']
    search_fields = ['title']

admin.site.register(Talk, TalkAdmin)

"""
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'talk')

admin.site.register(Vote, VoteAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'talk')

admin.site.register(Favorite, FavoriteAdmin)
"""
