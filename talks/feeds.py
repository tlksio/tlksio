from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Talk

class LatestTalksFeed(Feed):
    title = "Latest Talks"
    link = "/latewst"
    description = "Latest talks on vtalks.net"

    def itesm(self):
        print("foooooooo")
        return Talk.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

