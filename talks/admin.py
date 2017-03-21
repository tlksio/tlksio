from django.contrib import admin

from .models import Talk
from .models import Vote
from .models import Favorite

admin.site.register(Talk)
admin.site.register(Vote)
admin.site.register(Favorite)