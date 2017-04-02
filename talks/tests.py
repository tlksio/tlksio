import pytz
from datetime import datetime

from django.test import TestCase

from .models import Talk


class TalkTests(TestCase):

    def test_create_tag(self):
        talk = Talk()
        talk.created = datetime.now(pytz.utc)
        talk.updated = datetime.now(pytz.utc)
        talk.save()

        self.assertIs(Talk.objects.all().count(), 1)

