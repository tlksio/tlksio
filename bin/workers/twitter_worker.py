#!/usr/bin/env python

import os
import sys
import django
import twitter

sys.path.append("/home/raul/tlksio")
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

from talks.models import Talk
talk = Talk.objects.order_by('?').first()

api = twitter.Api(consumer_key=os.environ['CONSUMER_TOKEN'],
                  consumer_secret=os.environ['CONSUMER_SECRET'],
                  access_token_key=os.environ['ACCESS_TOKEN'],
                  access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

tweet = ""
tweet = "via @"+talk.author.username

print(tweet)

#status = api.PostUpdate('fooo')
#print(status)
