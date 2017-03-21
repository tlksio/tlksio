from django.contrib import admin

from .models import Talk
from .models import Vote
from .models import Favorite


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    list_filter = ['created']
    search_fields = ['title']

admin.site.register(Talk, TalkAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'talk')

admin.site.register(Vote, VoteAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'talk')

admin.site.register(Favorite, FavoriteAdmin)
